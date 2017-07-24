import os
import codecs
import numpy as np
import matplotlib.pyplot as plt
from Meth_blue_06_09 import get_cv_data
from Meth_blue_06_09 import calculate_graph_data
from Meth_blue_06_09 import get_data_paths


def main():
    directory = "/Users/st659/Google Drive/Meth Blue 4-10-16"

    paths = get_data_paths(directory)

    print(paths)

    sub_bw_anti_3, bw_anti_3, legend1= calculate_graph_data(paths[3:6])
    sub_bw_noanti_3, bw_noanti_3, legend2 = calculate_graph_data(paths[6:9])
    sub_pk_anti_3, pk_anti_3, legend3 = calculate_graph_data(paths[9:12])
    sub_pk_noanti_3, pk_noanti_3, legend4 = calculate_graph_data(paths[12:15])

    bw_mean = np.array([bw_anti_3[1], bw_noanti_3[1]])
    pk_mean = np.array([pk_anti_3[1], pk_noanti_3[1]])
    total_mean_matrix = np.array([bw_anti_3[1], bw_noanti_3[1], pk_noanti_3[1], pk_anti_3[1]])
    
    # mean_var = np.var(total_mean_matrix, axis=0)
    # bw_var = np.var(bw_mean, axis=0)
    # pk_var = np.var(pk_mean, axis=0)
    # print(len(mean_var))
    #
    # figure_var = plt.figure()
    # ax_var = figure_var.add_subplot(111)
    # ax_var.plot(bw_noanti_3[0], mean_var, label='Total')
    # ax_var.plot(bw_noanti_3[0],bw_var, label='BW')
    # ax_var.plot(bw_noanti_3[0],pk_var, label='PK')
    # plt.legend(loc= 'upper right')

    plt.style.use(['seaborn-white', 'seaborn-notebook'])

    diff = np.subtract(sub_bw_anti_3[1], sub_bw_noanti_3[1])
    diff_std = np.sqrt(np.add(np.square(sub_bw_anti_3[2]), np.square(sub_bw_noanti_3[2])))
    diff2 = np.subtract(sub_pk_anti_3[1], sub_pk_noanti_3[1])
    diff2_std = np.sqrt(np.add(np.square(sub_pk_anti_3[2]), np.square(sub_pk_noanti_3[2])))


    figure1 = plt.figure()
    ax1 = figure1.add_subplot(211)
    ax1.errorbar(sub_bw_anti_3[0], sub_bw_anti_3[1], sub_bw_anti_3[2], label=legend1)
    ax1.errorbar(sub_bw_noanti_3[0], sub_bw_noanti_3[1], sub_bw_noanti_3[2], label=legend2)
    ax1.set_ylabel('Current (mA)')
    ax1.set_xlabel('Voltage (V)')
    plt.legend(loc = 'upper left')
    ax2 = figure1.add_subplot(212)
    ax2.errorbar(sub_pk_anti_3[0], sub_pk_anti_3[1], sub_pk_anti_3[2], label=legend3)
    ax2.errorbar(sub_pk_noanti_3[0], sub_pk_noanti_3[1], sub_pk_noanti_3[2], label=legend4)
    ax2.set_ylabel('Current (mA)')
    ax2.set_xlabel('Voltage (V)')
    plt.legend(loc = 'upper left')

    plt.show()
    #
    # figure2 = plt.figure()
    # ax3 = figure2.add_subplot(211)
    # ax3.errorbar(sub_bw_anti_3[0], diff, diff_std, label='BW', color='b')
    # ax3.set_ylabel('$\Delta$ Current (mA)')
    #
    #
    # plt.legend(loc = 'upper left')
    # ax4 = figure2.add_subplot(212)
    # ax4.errorbar(sub_bw_anti_3[0], diff2, diff2_std, label='PK', color='g')
    # ax4.set_ylabel('$\Delta$ Current (mA)')
    # ax4.set_xlabel('Voltage (V)')
    # plt.legend(loc = 'upper left')
    # plt.show()

if __name__ == '__main__':
    main()