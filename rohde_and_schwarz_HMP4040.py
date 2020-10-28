"""
@author: aunal
"""

class HMP4040(object):
 
    def __init__(self, resource_manager, address):
        """
        resource_manager represents a function of visa module.
        Without resource manager, program can not communicate with instrument.
        An example for address of instrument : 'ASRL5::INSTR'
        """
        self.power_sup = resource_manager.open_resource(address, send_end = True)
        self.power_sup.write("*CLS")
        self.power_sup.write("*RST")
        
    def select_channel(self, channel_number):
        self.power_sup.write("INSTrument OUT{}".format(channel_number))

    def set_voltage_value(self, volt_value):
        """ 
        This function sets voltage level of selected channel.
        """
        self.power_sup.write("SOURce:VOLTage:LEVel:IMMediate:AMPLitude {}".format(volt_value))

    def set_current_value(self, curr_value):
        """ 
        This function sets current level of selected channel.
        """
        self.power_sup.write("SOURce:CURRent:LEVel:IMMediate:AMPLitude {}".format(curr_value))
    
    def set_voltage_current_value(self, volt, curr):
        """
        Sets both voltage and current
        """
        self.power_sup.write("APPLy {},{}".format(volt, curr))
    
    def turn_on_off_output(self, out):
        """
        This function sets selected output as on or off
        """
        self.power_sup.write("OUTPut:STATe {}".format(out))

    def IDN(self):
        """
        Ask instrument its name.
        """
        idn = self.power_sup.query("*IDN?")
        return idn

    def send_command(self, command):
        """
        Command variable can take any command, but it should be written in true format as in the manual.
        """
        self.power_sup.write("{}".format(command))
    
    def read_command_output(self):
        """
        After command, it reads output of the instrument and return what it read.
        """
        reading = self.power_sup.read()
        return reading

    """
    For more function, please have a look rohde & schwarz hmp4040 manual.
    """