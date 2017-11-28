from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class MCP4725(ArduinoObject):
    cfg_h_name = 'USE_MCP4725'

    def __init__(self, dac, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', dac)

    @arduinoobjectmethod
    def setVoltage(self, voltage, save=False):
        pass
