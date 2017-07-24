import matplotlib.pyplot as plt
from Meth_blue_06_09 import get_data_paths
from EIS_Reader import EISReader
import os

directory = '/Users/st659/Google Drive/ITO Impedance'
paths = get_data_paths(directory)
plt.style.use(['seaborn-white', 'seaborn-notebook'])
figure = plt.figure()
ax = figure.add_subplot(111)
ax2 = ax.twinx()
legends = ['APTES 100mM PB','APTES 10mM PB','100mM PB','10mM PB']
colour = ['r','g', 'b', 'k']
for file, col, leg in zip(paths,colour, legends):
    reader = EISReader(file)
    print(file)
    ax.loglog(reader.eis.frequency, reader.eis.magnitude, color=col)
    ax2.semilogx(reader.eis.frequency, reader.eis.phase, linestyle='--', color=col, label=leg)
    print(len(reader.eis.frequency))

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Mag ($\Omega$)')
ax2.set_ylabel('Phase (degrees)')
ax.legend(legends,loc=7)

plt.savefig(os.path.join(directory,'ITO Char.png'), dpi=300)

plt.show()