from EC_Lab_CVReader import get_data_paths
from EIS_Reader import EISReader
import matplotlib.pyplot as plt
import itertools
import os
from EIS_Reader import EISReader

before_directory = 'E:\\Chrome Download\\Ferrocene\\Wafer 1'
after_directory = 'E:\\Chrome Download\\Ferrocene\\SAM Impedance\\After'


before = get_data_paths(before_directory)
after = get_data_paths(after_directory)

plt.style.use(['seaborn-white', 'seaborn-notebook'])
fig = plt.figure()
#ax = fig.add_subplot(121)
ax2 = fig.add_subplot(111)
ax3 = ax2.twinx()



for eis_path in before:
    eis_reader = EISReader(eis_path)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')



ax2.set_xlabel('Frequency (Hz)')
ax2.legend(['Structured', 'Flat'], loc = 'upper center')
ax2.set_ylabel('Magnitude ($\Omega$)')
ax3.set_ylabel('Phase (degrees)')
fig.subplots_adjust(wspace = 0.3)
plt.savefig(os.path.join(before_directory,'wafer 1.png'), dpi=300)
plt.show()