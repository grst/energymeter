#!/usr/bin/env python3

from RPi import GPIO
import yaml
from functools import partial
from threading import Event

from sqlalchemy import create_engine, Column, DateTime, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import sys
from queue import Queue

Base = declarative_base()


class Pulse(Base):
    __tablename__ = "pulses"

    meter_id = Column(String(20), nullable=False, index=True, primary_key=True)
    time = Column(
        DateTime, nullable=False, default=datetime.utcnow, index=True, primary_key=True
    )


if __name__ == "__main__":
    with open("./config.yml") as f:
        CONFIG = yaml.safe_load(f)

    # setup sqlalchemy
    engine = create_engine(CONFIG["db_con"])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    pulse_queue = Queue()

    GPIO.setmode(GPIO.BCM)

    def pulse_callback(_, *, meter_id=None):
        # Example: Add a new Pulse to the database
        print(f"{meter_id}\t{datetime.utcnow().isoformat()}")
        new_pulse = Pulse(meter_id=meter_id, time=datetime.utcnow())
        pulse_queue.put(new_pulse)


    for meter_id, params in CONFIG["meters"].items():
        sys.stderr.write(f"Setting up meter '{meter_id}' on GPIO {params['GPIO']}\n")
        GPIO.setup(params["GPIO"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(
            params["GPIO"],
            GPIO.FALLING,
            callback=partial(pulse_callback, meter_id=meter_id),
        )

    while True:
        new_pulse = pulse_queue.get()
        try:
            session.add(new_pulse)
            session.commit()
        except SQLAlchemyError as e:
            sys.stderr.write(f"Exception when writing to database: {e}")
