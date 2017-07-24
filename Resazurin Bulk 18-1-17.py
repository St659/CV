from Meth_blue_06_09 import get_data_paths, calculate_graph_data
import matplotlib.pyplot as plt
import os
import numpy as np


def plot_cv_data(blank,path, ax):

    sub_data_2, data, legend = calculate_graph_data(path)
    blank_data, blank, legend = calculate_graph_data(blank)

    #Normalises results to blank and squares
    #sub_data_2[1][:] = [np.square(data - blank) for data, blank in zip(sub_data_2[1], blank_data[1])]
    #sub_data_2[2][:] = [np.square(data + blank) for data, blank in zip(sub_data_2[2], blank_data[2])]
    legend_str = path[0].split('/')[-1]
    legend = legend_str.split('_')[0]
    ax.plot(sub_data_2[0], sub_data_2[1])

directory = '/Users/st659/Google Drive/Resazurin Bulk 18-1-17'
plt.style.use(['seaborn-white', 'seaborn-notebook'])

paths = get_data_paths(directory)

sorted_paths = [paths[x:x+3] for x in range(0, len(paths), 3)]

fig = plt.figure()
ax = fig.add_subplot(111)

data = [plot_cv_data(sorted_paths[0],path, ax) for path in sorted_paths]

legends = ["Blank", 'Ecoli MG1655 $10^{4}$ cfu/ml', 'Ecoli MG1655 $10^{5}$ cfu/ml', 'Ecoli MG1655 $10^{6}$ cfu/ml']

plt.legend(legends,loc = 'lower right')
plt.ylabel('Current (mA)')
plt.xlabel('Voltage vs AgAgCl (V)')
plt.savefig(os.path.join(directory,'ResazurinBulk_18-1-17.png'), dpi=300)
plt.show()

