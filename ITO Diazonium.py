from Meth_blue_06_09 import get_data_paths, calculate_graph_data
from EIS_Reader import EISReader
import matplotlib.pyplot as plt
import os

directory = '/Users/st659/Google Drive/ITO Diazonium'

paths = get_data_paths(directory)

plt.style.use(['seaborn-white', 'seaborn-notebook'])
fig = plt.figure()
ax = fig.add_subplot(111)

print(len(paths))
for path in paths:
    sub_data_2, data, legend = calculate_graph_data(path)

    legend_str = path.split('/')[-1]
    print(legend_str)
    leg= legend_str.split('.')[0]
    print(legend)
    ax.plot(sub_data_2[0], sub_data_2[1], label=leg)

plt.title('Electrografting of Diazonium Salts to ITO')
plt.ylabel('Current (mA)')
plt.xlabel('Voltage (V)')
plt.legend(loc = 'upper left')
plt.savefig(os.path.join(directory,'ITO_Diaz-22-2-17.png'), dpi=300)
plt.show()