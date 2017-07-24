from Meth_blue_06_09 import get_data_paths, calculate_graph_data
import matplotlib.pyplot as plt
import os

directory = '/Users/st659/Google Drive/Resazurin Growth 11-1-17'
directory2 = '/Users/st659/Google Drive/Resazurin Pseudo 11-1-17'

paths = get_data_paths(directory)
paths_2 = get_data_paths(directory2)
blank = paths[:2]
mg = paths[2:]

blank_pseudo = paths_2[:2]
mg_pseudo = paths_2[2:]

print(blank)
plt.style.use(['seaborn-white', 'seaborn-notebook'])
data_list = list()
data_list_2 = list()

paths_list = [blank,mg]
paths_list_2 = [blank_pseudo, mg_pseudo]

# fig = plt.figure()
fig2 = plt.figure()

# ax = fig.add_subplot(111)
ax2 = fig2.add_subplot(111)

# for path in paths_list:
#     sub_data, data, legend = calculate_graph_data(path)
#     data_list.append(sub_data)
#     legend_str = path[0].split('/')[-1]
#     legend = legend_str.split('_')[0]
#     ax.errorbar(sub_data[0], sub_data[1],sub_data[2], label = legend)
#
# plt.xlim((-0.6,0))
# plt.ylim((-0.06, 0.02))
# plt.legend(loc = 'lower right')
# plt.title('Electrochemical Detection of E.coli MG1655 starting at 10^5 CFU/ml after 5 hours Incubation with 1mM Resazurin')
# plt.ylabel('Current (mA)')
# plt.xlabel('Voltage vs AgAgCl (V)')
# plt.savefig(os.path.join(directory,'ResazurinGrowth_11-1-17.png'), dpi=300)

for path in paths_list_2:
    sub_data_2, data, legend = calculate_graph_data(path)
    data_list_2.append(sub_data_2)
    legend_str = path[0].split('/')[-1]
    legend = legend_str.split('_')[0]
    ax2.plot(sub_data_2[0], sub_data_2[1], label = legend)

#plt.xlim((-0.6,0))
#plt.ylim((-0.06, 0.02))
plt.legend(loc = 'lower right')
plt.title('E.coli MG1655 Pseudo starting at 10^5 CFU/ml after 5 hours Incubation with 1mM Resazurin')
plt.ylabel('Current (mA)')
plt.xlabel('Voltage vs AgAgCl (V)')
plt.savefig(os.path.join(directory2,'ResazurinPseudo_11-1-17.png'), dpi=300)
plt.show()
