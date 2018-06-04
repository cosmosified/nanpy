from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

BME280_I2CADDR = 0x77

class BME280(ArduinoObject):
    cfg_h_name = 'USE_BME280'

    def __init__(self, address=BME280_I2CADDR, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', address)

    @returns(float)
    @arduinoobjectmethod
    def get_temperature(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def get_pressure(self):
        pass

    @returns(float)
    @arduinoobjectmethod
    def get_humidity(self):
        pass
