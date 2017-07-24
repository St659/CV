from Meth_blue_06_09 import get_data_paths, calculate_graph_data
import matplotlib.pyplot as plt
import itertools
import os
from EIS_Reader import EISReader

cv_directory = '/Users/st659/Google Drive/TiN ITO Comp 06-03-17/CV'
eis_directory = '/Users/st659/Google Drive/TiN ITO Comp 06-03-17/EIS'


cv_paths = get_data_paths(cv_directory)
eis_paths = get_data_paths(eis_directory)

plt.style.use(['seaborn-white', 'seaborn-notebook'])
fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax3 = ax2.twinx()

print(len(eis_paths))
for eis_path, cv_path in itertools.zip_longest(eis_paths,cv_paths):
    try:
        sub_data_2, data, legend = calculate_graph_data(cv_path)
        legend_str = cv_path.split('/')[-1]
        leg= legend_str.split(' ')[0]

        ax.plot(sub_data_2[0], sub_data_2[1], label=leg)
    except TypeError:
        print('All CV files used')

    eis_reader = EISReader(eis_path)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')


ax.legend(loc = 'lower right')
ax.set_ylabel('Current (mA)')
ax.set_xlabel('Voltage (V) vs Ag/AgCl')
ax2.set_xlabel('Frequency (Hz)')
ax2.legend(['TiN 10mM PB', 'TiN 100mM PB', 'ITO 10mM PB', 'ITO 100mM PB'], loc = 'lower right')
ax2.set_ylabel('Magnitude ($\Omega$)')
ax3.set_ylabel('Phase (degrees)')
fig.subplots_adjust(wspace = 0.3)
plt.savefig(os.path.join(cv_directory,'ITO_TiN_Comp_06-03-17.png'), dpi=300)
plt.show()