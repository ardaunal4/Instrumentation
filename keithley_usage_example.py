# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:31:50 2020

@author: aunal
"""

from keithley_class import Keithley # From python file import Keithley Class
import pyvisa # Import Pyvisa
from time import sleep

rm = pyvisa.ResourceManager() # Open Resource Manager

keithley_address = 'ASRL4::INSTR' # Address of instrument

keith = Keithley(rm, keithley_address) # Connect Keithley via pyvisa and prologix

print(keith.IDN()) # ask ID of instrument

keith.keithley_specifications() # Specify measurement style
#keith.keithley_specifications(function = 'CURRent:DC') # Specify measurement style

keith.send_command(":FETCh?")
print(keith.read_command_output())

keith.send_command(":STATus:CLEar") # Clears all messages from Error Queue

i = 1

while True:
    
    keith.close_channel(i)
    sleep(1)
    print("channel {} = ".format(i))
    print(keith.read_data())
    i += 1
    if  i == 5:
        i = 1
    