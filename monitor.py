#!/usr/bin/env python3

from RPi import GPIO
import yaml
import datetime
import time
from functools import partial
from threading import Event

def pulse_callback(channel, *, meter_id = None):
    print(f"Pulse on {meter_id} at {datetime.datetime.utcnow().isoformat()}")

if __name__ == "__main__":
    with open("./config.yml") as f:
        CONFIG = yaml.safe_load(f)
    
    GPIO.setmode(GPIO.BCM)

    for meter_id, params in CONFIG["meters"].items():
        print(f"Setting up meter '{meter_id}' on GPIO {params['GPIO']}")
        GPIO.setup(params["GPIO"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(params["GPIO"], GPIO.FALLING, callback=partial(pulse_callback, meter_id=meter_id))

    event = Event()
    event.wait()