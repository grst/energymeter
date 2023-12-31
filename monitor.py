#!/usr/bin/env python3

from RPi import GPIO
import yaml
import datetime
import time

with open("./config.yml") as f:
    CONFIG = yaml.safe_load(f)
print(CONFIG)

PIN = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def pulse_callback(channel):
    print(f"Pulse at {datetime.datetime.utcnow().isoformat()}")

 
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=pulse_callback)

while True:
    time.sleep(0.1)
