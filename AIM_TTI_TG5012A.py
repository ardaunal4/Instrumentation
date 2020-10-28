"""
@author: aunal
"""

class TG5012A(object):
    
    def __init__(self, resource_manager, address):
        """
        resource_manager represents a function of visa module.
        Without resource manager, program can not communicate with instrument.
        An example for address of instrument : 'TCPIP::128.141.154.197::9221::SOCKET'
        """
        self.pg = resource_manager.open_resource(address)
        self.pg.write_termination = '\n'
        self.pg.read_termination = '\r\n' 

    def choose_channel(self, channel_number):
        self.pg.write("CHN {}".format(channel_number))

    def choose_wave_type(self, wave_type):
        """ 
            wave_type variable stands for function of Pulse Generator.
            Functions should be written inside funcion when function called.
            Some of the functions listed below:
            1. TRIANG
            2. PULSE
            3. NOISE
            4. SQUARE
            5. SINE
            6. RAMP
        """
        self.pg.write("WAVE {}".format(wave_type))
    
    def frequency(self, freq):
        self.pg.write("FREQ {}".format(freq))

    def period(self, per):
        self.pg.write("PER {}".format(per))
    
    def amplitude_range(self, amp_range):
        """
        Set amplitude range ; auto
        """
        self.pg.write("AMPLRNG {}".format(amp_range))
        
    def amplitude_unit(self, amp_unit):
        """
        Amplitude units are VPP, VRMS and DBM
        """
        self.pg.write("AMPUNIT {}".format(amp_unit))
    
    def amplitude(self, amplitude):
        self.pg.write("AMPL {}".format(amplitude))
    
    def dc_offset(self, dc_off):
        self.pg.write("DCOFFS {}".format(dc_off))

    def output_state(self, out):
        self.pg.write("OUTPUT {}".format(out))
    
    def output_load(self, zload):
        self.pg.write("ZLOAD {}".format(zload))
    
    def duty_cycle_for_square_wave(self, width):
        self.pg.write("SQRSYMM {}".format(width))
    
    def duty_cycle_for_ramp_wave(self, width):
        self.pg.write("RMPSYMM {}".format(width))

    def synchronous_output(self, state):
        self.pg.write("RMPSYMM {}".format(state))
    
    def synchronous_type(self, out_type):
        self.pg.write("SYNCTYPE {}".format(out_type))
    
    def phase(self, phase):
        self.pg.write("PHASE {}".format(phase))

    def IDN(self):
        """
        Ask instrument its name.
        """
        idn = self.pg.query("*IDN?")
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
    
    """
    For more function, please have a look AIM TTI TG5012A manual.
    """