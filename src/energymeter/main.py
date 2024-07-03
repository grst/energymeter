#!/usr/bin/env python3

import sys
from datetime import datetime
from functools import partial
from queue import Queue
from threading import Thread
from time import sleep

import yaml
from RPi import GPIO
from sqlalchemy.exc import SQLAlchemyError

from .db import Pulse, get_session


def _pulse_callback(_, *, queue: Queue, meter_id: str):
    """Callback function when an event is detected on a GPIO port"""
    print(f"{meter_id}\t{datetime.now(datetime.UTF).isoformat()}")
    new_pulse = Pulse(meter_id=meter_id, time=datetime.now(datetime.UTF))
    queue.put(new_pulse)


def watch_modbus(meter_id: str, register: int, type_, ip, queue: Queue, interval: int):
    """Monitor a modbus register at a fixed interval"""
    sys.stderr.write(f"Setting up meter '{meter_id}' for register {register} on {ip}\n")
    while True:
        res = query_register(register)
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


def main():
    GPIO.setmode(GPIO.BCM)

    with open("./config.yml") as f:
        CONFIG = yaml.safe_load(f)

    db_session = get_session(CONFIG["db_con"])
    # For communication between monitoring and writing threads
    event_queue = Queue()

    db_thread = Thread(target=events_to_database, kwargs={"queue": event_queue, "db_session": db_session})
    db_thread.start()

    for meter_id, params in CONFIG["meters"].items():
        if params["type"] == "Pulse":
            watch_gpio(meter_id, params["GPIO"], event_queue)
        elif params["type"] in ["Power", "CumulativePower"]:
            watch_modbus(params["modbus"], params["type"], params["ip"])
        else:
            raise ValueError(f"Invalid type for {meter_id}")


if __name__ == "__main__":
    main()
