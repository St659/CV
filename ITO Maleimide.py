from Meth_blue_06_09 import get_data_paths, calculate_graph_data
import matplotlib.pyplot as plt
import os
from EIS_Reader import EISReader

cv_directory = '/Users/st659/Google Drive/ITO Maleidium Functionalisation 6-3-17/CV'
eis_directory = '/Users/st659/Google Drive/ITO Maleidium Functionalisation 6-3-17/EIS'

cv_paths = get_data_paths(cv_directory)
eis_paths = get_data_paths(eis_directory)

plt.style.use(['seaborn-white', 'seaborn-notebook'])
fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax3 = ax2.twinx()


for cv_path, eis_path in zip(cv_paths,eis_paths):
    sub_data_2, data, legend = calculate_graph_data(cv_path)
    eis_reader = EISReader(eis_path)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')
    print(eis_reader.eis.frequency)
    legend_str = cv_path.split('/')[-1]
    print(legend_str)
    leg= legend_str.split('.')[0]
    leg = leg.split('_')[0]
    ax.plot(sub_data_2[0], sub_data_2[1], label=leg)

ax.set_title('B')
ax.legend(loc = 'lower right')
ax2.set_title('A')
ax.set_ylabel('Current (mA)')
ax.set_xlabel('Voltage (V) vs Ag/AgCl')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude ($\Omega$)')
ax3.set_ylabel('Phase (degrees)')
fig.subplots_adjust(wspace = 0.3)
plt.savefig(os.path.join(cv_directory,'ito_malemide-3-3-17.png'), dpi=300)
plt.show()