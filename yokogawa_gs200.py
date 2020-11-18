# -*- coding: utf-8 -*-

"""
@author: aunal
"""

class GS200(object):
    """
        This class serves to commincate with Yokogawa.
        It is possible to use this class with PyVisa.
    """

    def __init__(self, resource_manager, address):
        """
        resource_manager represents a function of visa module.
        Without resource manager, program can not communicate with instrument.
        Yokogawa communication was done by using internet protocol.
        An example for address of instrument : 'TCPIP0::dcctyoko1.cern.ch::inst0::INSTR'
        """
        self.gs = resource_manager.open_resource(address)
        self.gs.write_termination = '\n'
        self.gs.write(":SYSTem::REMote")
        self.gs.write("*CLS")
        self.gs.write(":SENSe:ZERO:EXECute")
        

    def function_of_yokogawa(self, function = 'CURRent', upper_range = 200E-3):
        """ 
            Function variable stands for function of Yokogawa.
            Functions should be written inside funcion when function called.
            Some of the functions are listed below:
            1. VOLTage
            2. CURRent
            More function can be found in the Yokogawa GS200 manual.
        """
        self.gs.write(":SOURce:FUNCtion {}".format(function))
    
    def output_of_yokogawa(self, output):
        """
        Make output ON or OFF
        """
        self.gs.write(":OUTP:STAT {}".format(output))

    def range_of_yokogawa(self, range_):
        """
        It can take 2 different string commands which are ON and OFF.
        If you set auto range OFF, then you can specify upper Yokogawa.
        These are the are specified ranges:
        1E-3
        10E-3
        100E-3
        200E-3
        """
        self.gs.write(":SOUR:Range {}".format(range_))

    def IDN(self):
        """
        Ask instrument its name.
        """
        idn = self.gs.query("*IDN?") + ' started succesfully!'
        return idn

    def send_command(self, command):
        """
        Command variable can take any command, but it should be written in true format as in the manual.
        """
        self.gs.write("{}".format(command))
    
    def read_command_output(self):
        """
        After command, it reads output of the instrument and return what it read.
        """
        reading = self.gs.read() 
        return reading

    def query_command(self, command):
        """
        Read after write function. It sends command and read response of instrument.
        """
        reading = self.gs.query("{}".format(command))
        return reading
    
    def source_protection(self, function, limit = "MAXimum"):
        """
        The limit of the voltage and current can be specified by using this command.
        Limit of source is Maximum by default.
        Maximum and minimum values can be found from manual.
        Function variable stands for voltage or current.
        """
        self.gs.write(":SOURce:PROTection:{} {}".format(function, limit))

    def set_soruce_level(self, level):
        """
        Source level can not exceed 200E-3!
        """
        self.gs.write(":SOUR:LEVel {}".format(level))

    def close_inst(self):
        """
        After broke communication one can connect again using connect_inst function.
        """
        self.gs.close()

    def connect_inst(self, resource_manager, address):
        """
        After close_inst, this function should use to reopen
        """
        self.gs = resource_manager.open_resource(address)