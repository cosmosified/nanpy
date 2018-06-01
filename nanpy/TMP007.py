from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

TMP007_CFG_1SAMPLE = 0x0000
TMP007_CFG_2SAMPLE = 0x0200
TMP007_CFG_4SAMPLE = 0x0400
TMP007_CFG_8SAMPLE = 0x0600
TMP007_CFG_16SAMPLE = 0x0800

TMP007_I2CADDR = 0x40

class TMP007(ArduinoObject):
    cfg_h_name = 'USE_TMP007'

    def __init__(self, address=TMP007_I2CADDR, sample_rate=TMP007_CFG_16SAMPLE, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', address, sample_rate)

    @returns(float)
    @arduinoobjectmethod
    def get_object_temperature(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def get_die_temperature(self):
        pass
