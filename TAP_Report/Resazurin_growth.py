from EC_Lab_CVReader import get_data_paths, CVReader
from matplotlib import pyplot as plt
import scipy.stats as sci
import numpy as np
directory_pb = './Data/Res_growth'
directory_shu = './Data/Res_SHU'

pb_paths = get_data_paths(directory_pb)
shu_paths = get_data_paths(directory_shu)
pb_paths.sort()
shu_paths.sort()
plt.style.use(['seaborn-white', 'seaborn-notebook'])
figure = plt.figure()
ax = figure.add_subplot(111)
# sub_bw_anti_3, bw_anti_3, = calculate_graph_data(paths[0:3])
# sub_bw_noanti_3, bw_noanti_3 = calculate_graph_data(paths[3:6])
# sub_pk_anti_3, pk_anti_3 = calculate_graph_data(paths[6:9])
# sub_pk_noanti_3, pk_noanti_3 = calculate_graph_data(paths[9:12])

susceptible = [pb_paths[:3],pb_paths[3:6], pb_paths[6:9],pb_paths[9:12]]
resistant = []


for pb in susceptible:
    susceptible_current = list()

    for file1 in pb:
        reader_pb = CVReader(file1)

        susceptible_current.append(reader_pb.current)


    mean_susceptible = np.mean(susceptible_current, axis=0)

    ax.plot(reader_pb.voltage, mean_susceptible)

ax.set_xlabel('Voltage (V vs Ag/AgCl)')
legends = ["Resazurin Only", 'Ecoli MG1655 $10^{4}$ cfu/ml', 'Ecoli MG1655 $10^{5}$ cfu/ml', 'Ecoli MG1655 $10^{6}$ cfu/ml']
ax.legend(legends)
ax.set_ylabel('Current (mA)')

#ax.legend(['+ Ampicillin', ' - Ampicillin'], prop={'size':8})
#plt.savefig(os.path.join(noapp_directory,'raw__bare_cv.png'), dpi=300)
plt.show()