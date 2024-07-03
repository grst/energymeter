#!/usr/bin/env python3

import sys
from datetime import datetime
from functools import partial
from importlib.resources import files
from queue import Queue
from threading import Thread
from time import sleep

import yaml
from modbus import Modbus, Register
from RPi import GPIO
from sqlalchemy.exc import SQLAlchemyError

from .db import CumulativePower, Power, Pulse, get_session

MODBUS_UNIT = 3


def _pulse_callback(_, *, queue: Queue, meter_id: str):
    """Callback function when an event is detected on a GPIO port"""
    print(f"{meter_id}\t{datetime.now(datetime.UTF).isoformat()}")
    new_pulse = Pulse(meter_id=meter_id, time=datetime.now(datetime.UTF))
    queue.put(new_pulse)


def watch_modbus(
    modbus_client: Modbus,
    meter_id: str,
    register: Register,
    result_type: type[Power] | type[CumulativePower],
    ip: str,
    queue: Queue,
    interval: int,
):
    """Monitor a modbus register at a fixed interval"""
    sys.stderr.write(f"Setting up meter '{meter_id}' for register {register} on {ip}\n")
    while True:
        value = modbus_client.read_modbus(register)
        queue.put(result_type(meter_id=meter_id, time=datetime.now(datetime.UTC), value=value))
        sleep(interval)


def watch_gpio(meter_id: str, port: int, queue: Queue):
    """Monitor a GPIO port via events"""
    sys.stderr.write(f"Setting up meter '{meter_id}' on GPIO {port}\n")
    GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(port, GPIO.FALLING, callback=partial(_pulse_callback, meter_id=meter_id, queue=queue))


def events_to_database(queue: Queue, db_session):
    """Thread that write elements from a Queue to the database"""
    while True:
        new_pulse = queue.get()
        try:
            db_session.add(new_pulse)
            db_session.commit()
        except SQLAlchemyError as e:
            sys.stderr.write(f"Exception when writing to database: {e}")


def _connect_to_modbus(configs: dict):
    """Go through all configs and make create one modbus connection for each unique IP"""
    modbus_connections = {}
    for params in configs.values():
        if "modbus" in params:
            ip = params["ip"]
            if ip not in modbus_connections:
                modbus_connections[ip] = Modbus(ip)
    return modbus_connections


def main():
    GPIO.setmode(GPIO.BCM)
    # For communication between monitoring and writing threads
    event_queue = Queue()

    with (files("energymeter") / "config.yml").open() as f:
        CONFIG = yaml.safe_load(f)

    db_session = get_session(CONFIG["db_con"])

    modbus_connections = _connect_to_modbus(CONFIG["meters"])

    db_thread = Thread(target=events_to_database, kwargs={"queue": event_queue, "db_session": db_session})
    db_thread.start()

    threads = []
    for meter_id, params in CONFIG["meters"].items():
        if params["type"] == "Pulse":
            watch_gpio(meter_id, params["GPIO"], event_queue)
        elif params["type"] in ["Power", "CumulativePower"]:
            tmp_thread = Thread(
                target=watch_modbus,
                kwargs={
                    "modbus_client": modbus_connections[params["ip"]],
                    "meter_id": meter_id,
                    "register": params["register"],
                    "type_": params["type"],
                    "queue": event_queue,
                    "inverval": CONFIG["inverval"],
                },
            )
            tmp_thread.start()
            threads.append(tmp_thread)
        else:
            raise ValueError(f"Invalid type for {meter_id}")

    # will wait forever, since this thread never finishes
    db_thread.join()


if __name__ == "__main__":
    main()
