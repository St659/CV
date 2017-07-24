from EC_Lab_CVReader import get_data_paths
from EIS_Reader import EISReader
import matplotlib.pyplot as plt
import itertools
import os
from EIS_Reader import EISReader

before_directory = 'E:\\Chrome Download\\Ferrocene\\SAM Impedance\\Before'
after_directory = 'E:\\Chrome Download\\Ferrocene\\SAM IS'


before = get_data_paths(before_directory)
after = get_data_paths(after_directory)

plt.style.use(['seaborn-white', 'seaborn-notebook'])
fig = plt.figure()
fig2 = plt.figure()
#ax = fig.add_subplot(121)
ax2 = fig.add_subplot(111)
ax3 = fig2.add_subplot(111)


for eis_path in after:
    eis_reader = EISReader(eis_path)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')

ax2.set_xlabel('Frequency (Hz)')
ax2.legend(['1', '2', '3', '4','5','6'], loc = 'upper right')
ax2.set_ylabel('Magnitude ($\Omega$)')
ax3.set_ylabel('Phase (degrees)')
ax3.set_xlabel('Frequency (Hz)')
#fig.subplots_adjust(wspace = 0.3)
#plt.savefig(os.path.join(cv_directory,'ITO_TiN_Comp_06-03-17.png'), dpi=300)
plt.show()