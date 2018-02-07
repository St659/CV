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
legends_lim = ['APTES 10mM PB','10mM PB']
colour = ['r','g', 'b', 'k']
colour_lim = ['r','b']
# for file, col, leg in zip(paths[3],colour_lim[1], legends_lim[1]):
#     reader = EISReader(file)
#     print(file)
#     ax.loglog(reader.eis.frequency, reader.eis.magnitude, color=col)
#     ax2.semilogx(reader.eis.frequency, reader.eis.phase, linestyle='--', color=col, label=leg)
#     print(len(reader.eis.frequency))


reader = EISReader(paths[1])

ax.loglog(reader.eis.frequency, reader.eis.magnitude, color='b')
ax2.semilogx(reader.eis.frequency, reader.eis.phase, linestyle='--', color='b', label='10mM PB')
print(len(reader.eis.frequency))
#EIS_plot_labels(ax,ax2)

ax.legend(['10mM PB'],loc=7)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('|Z| $\Omega$')
ax2.set_ylabel('$\\angle$ Z (degrees)')

#plt.savefig(os.path.join(directory,'ITO Char.png'), dpi=300)

plt.show()