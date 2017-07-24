import os
import matplotlib.pyplot as plt
import numpy as np
import codecs


def get_data(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:

        file_lines = file.readlines()
        file_list = list()

        x = list()
        y = list()


        for line in file_lines[51:]:

            split= line.split()

            x.append(split[6])
            y.append(split[11])

        for i, item in enumerate(y):
            if "XXX" in item:
                x.pop(i)
                y.pop(i)

        x_float = [float(i) for i in x]
        y_float = [float(i) for i in y]
        return np.asarray(y_float), np.asarray(x_float)


def calculate_graph_data(*args):
    ydata_list = list()
    data_files= args[0]
    print(data_files)
    for data_file in data_files:
        y1, x1 = get_data(data_file)
        ydata_list.append(y1)



    y_array = np.array(ydata_list)

    y_mean = np.mean(y_array, axis=0)
    y_std = np.std(y_array, axis=0)
    return y_mean, y_std, x1


filenames = os.listdir("Data")



paths = list()




for name in filenames:
    new_name = "Data/" + name
    paths.append(new_name)


blank, blank_err, x = calculate_graph_data(paths[:3])
bw_mean, bw_err, x = calculate_graph_data(paths[3:6])
bw_anti_mean, bw_anti_err, x = calculate_graph_data(paths[6:9])
pkd_mean, pkd_err, x = calculate_graph_data(paths[9:12])
pkd_anti_mean, pkd_anti_err, x = calculate_graph_data(paths[12:15])
# sus_noanti_mean, sus_noanti_err, x = calculate_graph_data(paths[9], paths[11])
#
#
#
#
# legend_names = {"Res Anti", "Res No Anti", "Sus Anti", "Sus No Anti"}
#
plt.hold(True)
plt.errorbar(x, blank, blank_err, color='b')
plt.errorbar(x, bw_mean, bw_err, color='r')
plt.errorbar(x, bw_anti_mean, bw_anti_err, color="g")
plt.errorbar(x, pkd_mean, pkd_err, color="k" )
plt.errorbar(x, pkd_anti_mean, pkd_anti_err,color="c" )
# plt.errorbar(x, sus_noanti_mean, sus_noanti_err, color="k" )
#
plt.show()
