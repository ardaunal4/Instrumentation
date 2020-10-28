# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:27:18 2020

@author: aunal
"""

from AIM_TTI_TG5012A import TG5012A
import pyvisa

rm = pyvisa.ResourceManager()

pulse_gen_address = 'TCPIP::dcct-pulse-generator.cern.ch::9221::SOCKET' # Address of instrument

pulse_gen = TG5012A(rm, pulse_gen_address) # Connect Keithley via pyvisa and prologix

print(pulse_gen.IDN()) # ask ID of instrument

pulse_gen.choose_channel(2)

pulse_gen.choose_wave_type('SQUARE')

pulse_gen.period(0.00009)

pulse_gen.amplitude(5)

pulse_gen.dc_offset(2.5)

pulse_gen.choose_channel(2)

pulse_gen.output_load(50)

pulse_gen.output_state('OFF')
#pulse_gen.amplitude_unit
