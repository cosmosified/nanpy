#!/usr/bin/env python

"""Tests the TMP007 sensor"""

import time
import logging
from nanpy import TMP007
from nanpy.serialmanager import SerialManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TMP007")

connection = SerialManager(sleep_after_connect=2)
connection.open()

sensor = TMP007(connection=connection)

try:
    while True:
        object_temp = sensor.get_object_temperature()
        die_temp = sensor.get_die_temperature()
        logger.info("Object temperature: %.2f", object_temp)
        logger.info("Die temperature: %.2f", die_temp)
        time.sleep(4)
except KeyboardInterrupt:
    pass
