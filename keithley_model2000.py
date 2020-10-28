"""
@author: aunal
"""

class Keithley(object):
    """
        This class serves to commincate with Keithley.
        I recommend to use at least 0.6 sec sleep function, after use write and read function!
    """

    def __init__(self, resource_manager, address):
        """
        resource_manager represents a function of visa module.
        Without resource manager, program can not communicate with instrument.
        An example for address of instrument : 'ASRL4::INSTR'
        """

        self.keith = resource_manager.open_resource(address)


    def keithley_specifications(self, function = 'VOLTage:DC', auto_range = 'ON', lower_range = -10, upper_range = 10):
        """ 
            Function variable stands for function of Keithley.
            Functions should be written inside funcion when function called.
            Some of the functions listed below:
            1. VOLTage:DC
            2. VOLTage:AC
            3. CURRent:DC
            4. CURRent:AC
            5. RESistance
            6. TEMPerature
            More function can be found in the Keithley 2000 manual.
            auto_range variable represents autoranging of the instrument.
            It can take 2 different string commands which are ON and OFF.
            If you set auto range OFF, then you can specify upper and lower range of Keithley.
        """
        self.keith.write(":SENSe:FUNCtion '{}'".format(function))
        self.keith.write("SENse:{}:RANGe:AUTO {}".format(function, auto_range))

        if auto_range == 'OFF':            
            self.keith.write("SENSe:{}:RANGe:UPPer {}".format(function, upper_range)) 
            self.keith.write("SENSe:{}:RANGe:LOWer {}".format(function, lower_range))
         
    def IDN(self):
        """
        Ask instrument its name.
        """

        self.keith.write("*IDN?")
        self.keith.write('++read eoi')
        reading = self.keith.read()        
        return reading

    def read_data(self):
        """
        When this function called, it is going to return the last instrument reading.
        """
        self.keith.write("SENse:DATA?")
        self.keith.write('++read eoi')
        output = self.keith.read()
        return output
    
    def close_channel(self, channel_no):
        """
        This function can be used if there is a multiplexer which connected to Keithley.
        When function called with channel_no variable, it closes choosen channel.
        """
        self.keith.write(":rout:close (@{})".format(channel_no))

    def send_command(self, command):
        """
        Command variable can take any command, but it should be written in true format as in the manual.
        """
        self.keith.write("{}".format(command))
    
    def read_command_output(self):
        """
        After command, it reads output of the instrument and return what it read.
        """
        self.keith.write('++read eoi') 
        reading = self.keith.read()
        return reading