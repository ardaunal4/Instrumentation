import pyvisa
from yokogawa_gs200 import GS200
from time import sleep

rm = pyvisa.ResourceManager()

address = 'TCPIP::128.141.153.162::INSTR'

current_source = GS200(rm, address)

print(current_source.IDN())

current_source.function_of_yokogawa(function='CURRent')

current_source.range_of_yokogawa(200E-3)

current_source.set_soruce_level(100E-3)

current_source.output_of_yokogawa('ON')

sleep(10)

current_source.output_of_yokogawa('OFF')