import nidaqmx
from nidaqmx import constants
from nidaqmx import stream_readers
import numpy as np

measTime = 10 # measurement time in seconds
rate = 10000 # sampling rate in Hz

with nidaqmx.Task() as task:
    # add channels to task
    task.ai_channels.add_ai_voltage_chan(physical_channel = 'Dev1/ai0', name_to_assign_to_channel = 'B', units = nidaqmx.constants.VoltageUnits.VOLTS)
    task.ai_channels.add_ai_voltage_chan(physical_channel = 'Dev1/ai1', name_to_assign_to_channel = 'H', units = nidaqmx.constants.VoltageUnits.VOLTS)
        
    # set sampling rate
    task.timing.cfg_samp_clk_timing(rate = rate, sample_mode = constants.AcquisitionType.CONTINUOUS, samps_per_chan = measTime * rate)
    
    # start tasks
    task.start() 

    # measure
    reader = stream_readers.AnalogMultiChannelReader(task.in_stream)  
    data = np.zeros((2, measTime * rate))    
    reader.read_many_sample(data, measTime * rate)

    # start tasks
    task.stop()
