from Meth_blue_06_09 import get_data_paths, calculate_graph_data
from matplotlib import pyplot as plt
import numpy as np
import os
def get_max_voltage(cv):
    current_arg = np.argmax(cv[2])
    voltage_max = cv[0][current_arg]
    return voltage_max

directory = 'E:\Google Drive\On Chip Meth Blue 14-12-16'
paths = get_data_paths(directory)
ecoli_paths = [paths[0],  paths[2]]
blank_paths = [paths[1], paths[4]]
sub_ecoli, ecoli,legend = calculate_graph_data(ecoli_paths)
sub_blank, blank, legend = calculate_graph_data(blank_paths )
figure = plt.figure()
ax = figure.add_subplot(111)

ax.plot(sub_blank[0], sub_blank[1])
#ax.errorbar(sub_ecoli[0], sub_ecoli[1], sub_ecoli[2])

blank_max_voltage = get_max_voltage(sub_blank)
ecoli_max_voltage = get_max_voltage(sub_ecoli)
voltage_shift = ecoli_max_voltage - blank_max_voltage
print('Voltage shift: ' + str(voltage_shift))
ph_shift = (voltage_shift*1000)/37
print('pH shift: ' + str(ph_shift))
bulkshift = 6.93 -6.34
print('pH Bulk:' + str(bulkshift))
ax.set_ylabel('Current (mA)')
ax.set_xlabel('Voltage vs Ag/AgCl (V)')
#plt.savefig(os.path.join(directory,'metblue.png'), dpi=300)

plt.show()