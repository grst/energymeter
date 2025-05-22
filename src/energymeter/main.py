#!/usr/bin/env python3

import sys
from datetime import datetime
from functools import partial
from importlib.resources import files
from queue import Queue
from threading import Thread
from time import sleep

import yaml
from RPi import GPIO
from sqlalchemy.exc import SQLAlchemyError

from ._util import _connect_to_modbus, _load_meters
from .db import get_session
from .meters import GPIOMeter, ModbusMeter
from .modbus import Modbus
from pymodbus.exceptions import ModbusException


def _pulse_callback(_, *, queue: Queue, meter: GPIOMeter):
    """Callback function when an event is detected on a GPIO port"""
    print(f"{meter.name}\t{meter.id}\t{datetime.utcnow().isoformat()}\t{1}")
    event = meter.get_event()
    queue.put(event)


def watch_gpio(meter: GPIOMeter, queue: Queue):
    """Monitor a GPIO port via events"""
    sys.stderr.write(f"Setting up meter '{meter.name}' with ID {meter.id} on GPIO {meter.gpio_port}\n")
    GPIO.setup(meter.gpio_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(meter.gpio_port, GPIO.FALLING, callback=partial(_pulse_callback, meter=meter, queue=queue))


def watch_modbus(
    meter: ModbusMeter,
    modbus_client: Modbus,
    queue: Queue,
    interval: int,
):
    """Monitor a modbus register at a fixed interval"""
    sys.stderr.write(
        f"Setting up meter '{meter.name}' with ID {meter.id} for register {meter.modbus_register_address} on {meter.ip_address}\n"
    )
    while True:
        try:
            value = modbus_client.read_modbus(meter.get_register(), unit=meter.unit)
            print(f"{meter.name}\t{meter.id}\t{datetime.utcnow().isoformat()}\t{value}")
            event = meter.get_event(value)
            queue.put(event)
        except (AttributeError, KeyError, OSError, ModbusException):
            pass
        sleep(interval)


def write_events_to_database(queue: Queue, db_session):
    """Thread that write elements from a Queue to the database"""
    while True:
        new_pulse = queue.get()
        try:
            with db_session() as session:
                session.add(new_pulse)
                session.commit()
        except SQLAlchemyError as e:
            sys.stderr.write(f"Exception when writing to database: {e}")


def main():
    GPIO.setmode(GPIO.BCM)
    # For communication between monitoring and writing threads
    event_queue = Queue()

    with (files("energymeter") / "config.yml").open() as f:
        CONFIG = yaml.safe_load(f)

    db_session = get_session(CONFIG["db_con"])

    modbus_meters: list[ModbusMeter] = _load_meters(CONFIG["meters"]["Modbus"], ModbusMeter, with_db_table=True)
    gpio_meters: list[GPIOMeter] = _load_meters(CONFIG["meters"]["GPIO"], GPIOMeter, with_db_table=True)
    assert len(modbus_meters) + len(gpio_meters) == len(
        {m.id for m in modbus_meters + gpio_meters}
    ), "Meter IDs not unique"
    modbus_connections = _connect_to_modbus(modbus_meters)

    db_thread = Thread(target=write_events_to_database, kwargs={"queue": event_queue, "db_session": db_session})
    db_thread.start()

    # # Start monitoring GPIO ports
    for meter in gpio_meters:
        watch_gpio(meter, event_queue)

    # Start monitoring modbus connections
    threads = []
    for meter in modbus_meters:
        tmp_thread = Thread(
            target=watch_modbus,
            kwargs={
                "modbus_client": modbus_connections[meter.ip_address],
                "meter": meter,
                "queue": event_queue,
                "interval": CONFIG["interval"],
            },
        )
        tmp_thread.start()
        threads.append(tmp_thread)

    # will wait forever, since this thread never finishes
    db_thread.join()


if __name__ == "__main__":
    main()
