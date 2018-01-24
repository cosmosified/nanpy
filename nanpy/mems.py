from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware


@check4firmware
class Mems(FirmwareClass):

    """Control a MEMS switch
    """
    firmware_id = 'Mems'
    cfg_h_name = 'USE_MEMS'

    @arduinomethod
    def begin(self, address=None):
        """Initialize the data bus
        """

    @returns(int)
    @arduinomethod
    def get_error_code(self, address):
        """Get the error code
        """

    @returns(int)
    @arduinomethod
    def get_firmware_version(self, address):
        """Get the firmware version
        """

    @returns(int)
    @arduinomethod
    def get_status(self, address):
        """Get the status
        """

    @returns(int)
    @arduinomethod
    def set_channel_number(self, address, channel):
        """Set the channel number

        Returns the status
        """

    @returns(int)
    @arduinomethod
    def get_device_dimensions(self, address):
        """Gets the device dimensions
        """
