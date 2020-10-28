# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:34:21 2020

@author: aunal
"""
from rohde_and_schwarz_HMP4040 import HMP4040
import pyvisa

rm = pyvisa.ResourceManager()

power_sup_address = 'ASRL5::INSTR' # Address of instrument

power_sup = HMP4040(rm, power_sup_address) # Connect Keithley via pyvisa and prologix

print(power_sup.IDN()) # ask ID of instrument

power_sup.select_channel(1) # select channel

power_sup.set_voltage_value(20) # set voltage level

power_sup.turn_on_off_output('ON') # Output ON/OFF

