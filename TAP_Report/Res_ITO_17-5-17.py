from EC_Lab_CVReader import get_data_paths, CVReader
from matplotlib import pyplot as plt
import scipy.stats as sci
import numpy as np
directory_pb = './Data/Res_PB'
directory_shu = './Data/Res_SHU'

pb_paths = get_data_paths(directory_pb)
shu_paths = get_data_paths(directory_shu)
pb_paths.sort()
shu_paths.sort()
plt.style.use(['seaborn-white', 'seaborn-notebook'])
figure = plt.figure()

ax = figure.add_subplot(121)
ax2 = figure.add_subplot(122)

for pb,shu in zip(pb_paths, shu_paths):

    reader_pb = CVReader(pb)
    reader_shu = CVReader(shu)

    ax.plot(reader_shu.voltage, reader_shu.current)
    ax2.plot(reader_pb.voltage, reader_pb.current)

ax.set_xlabel('Voltage (V vs Ag/AgCl)')
ax2.set_xlabel('Voltage (V vs Ag/AgCl)')
ax.set_ylabel('Current (mA)')

ax.legend(['20 mV/s','50 mV/s', '100 mV/s', '250 mV/s', '500 mV/s', '1000 mV/s', '2500 mV/s', '5000 mV/s'], prop={'size':8})
#plt.savefig(os.path.join(noapp_directory,'raw__bare_cv.png'), dpi=300)
plt.show()