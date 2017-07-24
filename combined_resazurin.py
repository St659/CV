from Meth_blue_06_09 import get_data_paths, calculate_graph_data
import matplotlib.pyplot as plt
import os


directory1 = '/Users/st659/Google Drive/Resazurin Growth 12-1-17'
directory2 = '/Users/st659/Google Drive/Resazurin Growth 11-1-17'
directory3 = '/Users/st659/Google Drive/Resazurin Growth 5-1-17'
plt.style.use(['seaborn-white', 'seaborn-notebook'])

paths1 = get_data_paths(directory1)
paths2 = get_data_paths(directory2)
paths3 = get_data_paths(directory3)

blank = paths1[:2]
mg4_paths = paths1[3:]
mg5_paths = paths2[2:]
mg6_paths = paths3[2:]

print(mg6_paths)
print(mg5_paths)
print(mg4_paths)
paths_list = [blank, mg4_paths, mg6_paths]

fig2 = plt.figure()

legends = ['Blank', 'E.coli MG1655 $10^{4}$ cfu/ml', 'E.coli MG1655 $10^{6}$ cfu/ml']

ax2 = fig2.add_subplot(111)


data_list = list()
for path in paths_list:
    sub_data_2, data, legend = calculate_graph_data(path)
    data_list.append(sub_data_2)
    legend_str = path[0].split('/')[-1]
    legend = legend_str.split('_')[0]
    ax2.errorbar(sub_data_2[0], sub_data_2[1], sub_data_2[2], label = legend)

ax2.legend(legends, loc='lower right')
ax2.set_ylabel('Current (mA)')
ax2.set_xlabel('Voltage vs Ag/AgCl (V)')

plt.xlim((-0.6, 0))
plt.ylim((-0.06, 0.02))

#plt.savefig(os.path.join(directory2,'Resazurin_OnChip.png'), dpi=300)
plt.show()