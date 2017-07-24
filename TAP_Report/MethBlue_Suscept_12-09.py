from EC_Lab_CVReader import get_data_paths, CVReader
from matplotlib import pyplot as plt
import scipy.stats as sci
import numpy as np
directory_pb = './Data/MB_Suscept'
directory_shu = './Data/Res_SHU'

pb_paths = get_data_paths(directory_pb)
shu_paths = get_data_paths(directory_shu)
pb_paths.sort()
shu_paths.sort()
plt.style.use(['seaborn-white', 'seaborn-notebook'])
figure, (ax, ax2)= plt.subplots(1,2,sharey=True)
# sub_bw_anti_3, bw_anti_3, = calculate_graph_data(paths[0:3])
# sub_bw_noanti_3, bw_noanti_3 = calculate_graph_data(paths[3:6])
# sub_pk_anti_3, pk_anti_3 = calculate_graph_data(paths[6:9])
# sub_pk_noanti_3, pk_noanti_3 = calculate_graph_data(paths[9:12])

susceptible = [pb_paths[:3],pb_paths[3:6]]
resistant = [pb_paths[6:9],pb_paths[9:12]]


for pb,shu in zip(susceptible, resistant):
    susceptible_current = list()
    resistant_current = list()
    for file1, file2 in zip(pb,shu):
        reader_pb = CVReader(file1)
        reader_shu = CVReader(file2)
        susceptible_current.append(reader_pb.current)
        resistant_current.append(reader_shu.current)

    mean_susceptible = np.mean(susceptible_current, axis=0)
    mean_resistant = np.mean(resistant_current, axis=0)
    ax.plot(reader_shu.voltage, mean_susceptible)
    ax2.plot(reader_pb.voltage, mean_resistant)

ax.set_xlabel('Voltage (V vs Ag/AgCl)')
ax2.set_xlabel('Voltage (V vs Ag/AgCl)')
ax.set_ylabel('Current (mA)')

ax.legend(['+ Ampicillin', ' - Ampicillin'], prop={'size':8})
#plt.savefig(os.path.join(noapp_directory,'raw__bare_cv.png'), dpi=300)
plt.show()