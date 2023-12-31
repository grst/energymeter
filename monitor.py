#!/usr/bin/env python3

from RPi import GPIO
import yaml
from functools import partial
from threading import Event

from sqlalchemy import create_engine, Column, DateTime, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import sys

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

    GPIO.setmode(GPIO.BCM)

    def pulse_callback(_, *, meter_id=None):
        # Example: Add a new Pulse to the database
        new_pulse = Pulse(meter_id=meter_id, time=datetime.utcnow())
        session.add(new_pulse)
        session.commit()
        print(f"{meter_id}\t{datetime.utcnow().isoformat()}")

    for meter_id, params in CONFIG["meters"].items():
        sys.stderr.write(f"Setting up meter '{meter_id}' on GPIO {params['GPIO']}\n")
        GPIO.setup(params["GPIO"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(
            params["GPIO"],
            GPIO.FALLING,
            callback=partial(pulse_callback, meter_id=meter_id),
        )

    # Wait indefinitely
    event = Event()
    event.wait()
