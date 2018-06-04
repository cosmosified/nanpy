#!/usr/bin/env python

"""Tests the BME280 sensor"""

import time
import logging
from nanpy import BME280
from nanpy.serialmanager import SerialManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BME280")

connection = SerialManager(sleep_after_connect=2)
connection.open()

sensor = BME280(connection=connection)

try:
    while True:
        temperature = sensor.get_temperature()
        pressure = sensor.get_pressure()
        humidity = sensor.get_humidity()
        logger.info("Temperature: %.2f", temperature)
        logger.info("Pressure: %.2f", pressure)
        logger.info("Humidity: %.2f", humidity)
        time.sleep(1)
except KeyboardInterrupt:
    pass
