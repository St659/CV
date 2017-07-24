import os
import codecs
import numpy as np
import matplotlib.pyplot as plt
from Meth_blue_06_09 import get_cv_data
from Meth_blue_06_09 import calculate_graph_data
from Meth_blue_06_09 import get_data_paths


def main():
    directory = "/Users/st659/Google Drive/Meth Blue 12-09"
    
    paths = get_data_paths(directory)

    plt.style.use(['seaborn-white', 'seaborn-notebook'])

    print(paths)

    # sub_bw_anti_3, bw_anti_3, = calculate_graph_data(paths[0:3])
    # sub_bw_noanti_3, bw_noanti_3 = calculate_graph_data(paths[3:6])
    # sub_pk_anti_3, pk_anti_3 = calculate_graph_data(paths[6:9])
    # sub_pk_noanti_3, pk_noanti_3 = calculate_graph_data(paths[9:12])
    #
    # figure1 = plt.figure()
    # ax1 = figure1.add_subplot(111)
    # ax1.errorbar(sub_bw_anti_3[0], sub_bw_anti_3[1], sub_bw_anti_3[2])
    # ax1.errorbar(sub_bw_noanti_3[0], sub_bw_noanti_3[1], sub_bw_noanti_3[2])
    # ax1.errorbar(sub_pk_anti_3[0], sub_pk_anti_3[1], sub_pk_anti_3[2])
    # ax1.errorbar(sub_pk_noanti_3[0], sub_pk_noanti_3[1], sub_pk_noanti_3[2])
    #
    # plt.xlabel('Voltage vs reference (V)')
    # plt.ylabel('Current (mA)')
    # plt.xlim([-0.3, 0])
    # plt.ylim([-0.02, 0.01])
    # plt.legend(('BW25113 0$\mu g/ml$ Ampicillin', 'BW25133 50$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 0$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 50$\mu g/ml$ Ampicillin'),loc='lower right', fontsize = '10')
    # plt.title(r'Antibiotic Susceptibility of $10^{3}$ Bacteria after 5 hours incubation')
    
    
    # sub_bw_anti_4, bw_anti_4, l= calculate_graph_data(paths[12:15])
    # sub_bw_noanti_4, bw_noanti_4, l = calculate_graph_data(paths[15:18])
    # sub_pk_anti_4, pk_anti_4, l = calculate_graph_data(paths[18:21])
    # sub_pk_noanti_4, pk_noanti_4, l = calculate_graph_data(paths[21:24])
    #
    # figure2 = plt.figure()
    # ax2 = figure2.add_subplot(111)
    # ax2.errorbar(sub_bw_anti_4[0], sub_bw_anti_4[1], sub_bw_anti_4[2])
    # ax2.errorbar(sub_bw_noanti_4[0], sub_bw_noanti_4[1], sub_bw_noanti_4[2])
    # ax2.errorbar(sub_pk_anti_4[0], sub_pk_anti_4[1], sub_pk_anti_4[2])
    # ax2.errorbar(sub_pk_noanti_4[0], sub_pk_noanti_4[1], sub_pk_noanti_4[2])
    #
    # plt.xlabel('Voltage vs reference (V)')
    # plt.ylabel('Current (mA)')
    # plt.xlim([-0.3, 0])
    # plt.ylim([-0.02, 0.01])
    # plt.legend(('BW25113 50$\mu g/ml$ Ampicillin', 'BW25133 0$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 50$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 0$\mu g/ml$ Ampicillin'),loc='lower right', fontsize = '10')
    # plt.title(r'Antibiotic Susceptibility of $10^{4}$ CFU/ml after 5 hours incubation')
    # #plt.savefig(os.path.join(directory,'susceptibility 10_4.png'), dpi=1200)
    #
    # diff = np.subtract(sub_bw_anti_4[1], sub_bw_noanti_4[1])
    # diff_std = np.sqrt(np.add(np.square(sub_bw_anti_4[2]), np.square(sub_bw_noanti_4[2])))
    # diff2 = np.subtract(sub_pk_anti_4[1], sub_pk_noanti_4[1])
    # diff2_std = np.sqrt(np.add(np.square(sub_pk_anti_4[2]), np.square(sub_pk_noanti_4[2])))
    #
    # figure2 = plt.figure()
    # ax3 = figure2.add_subplot(211)
    # ax3.errorbar(sub_bw_anti_4[0], diff, diff_std, label='BW', color='b')
    # ax3.set_ylabel('$\Delta$ Current (mA)')
    #
    # plt.legend(loc = 'upper left')
    # ax4 = figure2.add_subplot(212)
    # ax4.errorbar(sub_bw_anti_4[0], diff2, diff2_std, label='PK', color='g')
    # ax4.set_ylabel('$\Delta$ Current (mA)')
    # ax4.set_xlabel('Voltage (V)')
    # plt.legend(loc = 'upper left')
    #
    #
    #
    #
    # sub_bw_anti_5, bw_anti_5, l = calculate_graph_data(paths[24:27])
    # sub_bw_noanti_5, bw_noanti_5, l = calculate_graph_data(paths[27:30])
    # sub_pk_anti_5, pk_anti_5, l = calculate_graph_data(paths[30:33])
    # sub_pk_noanti_5, pk_noanti_5, l = calculate_graph_data(paths[33:36])
    #
    # mean_matrix = np.array([bw_anti_5[1], bw_noanti_5[1], pk_noanti_5[1], pk_anti_5[1]])
    # mean_var = np.var(mean_matrix, axis=0)
    # print(len(mean_var))
    #
    # figure_var = plt.figure()
    # ax_var = figure_var.add_subplot(111)
    # ax_var.plot(bw_noanti_5[0], mean_var)
    # plt.show()
    
    # diff = np.subtract(sub_bw_anti_5[1], sub_bw_noanti_5[1])
    # diff_std = np.sqrt(np.add(np.square(sub_bw_anti_5[2]), np.square(sub_bw_noanti_5[2])))
    # diff2 = np.subtract(sub_pk_anti_5[1], sub_pk_noanti_5[1])
    # diff2_std = np.sqrt(np.add(np.square(sub_pk_anti_5[2]), np.square(sub_pk_noanti_5[2])))
    #
    # figure3 = plt.figure()
    # ax5 = figure3.add_subplot(211)
    # ax5.errorbar(sub_bw_anti_4[0], diff, diff_std, label='BW', color='b')
    # ax5.set_ylabel('$\Delta$ Current (mA)')
    #
    # plt.legend(loc = 'upper left')
    # ax6 = figure3.add_subplot(212)
    # ax6.errorbar(sub_bw_anti_4[0], diff2, diff2_std, label='PK', color='g')
    # ax6.set_ylabel('$\Delta$ Current (mA)')
    # ax6.set_xlabel('Voltage (V)')
    # plt.legend(loc = 'upper left')
    #
    # figure3 = plt.figure()
    # ax3 = figure3.add_subplot(111)
    # ax3.errorbar(sub_bw_anti_5[0], sub_bw_anti_5[1], sub_bw_anti_5[2])
    # ax3.errorbar(sub_bw_noanti_5[0], sub_bw_noanti_5[1], sub_bw_noanti_5[2])
    # ax3.errorbar(sub_pk_anti_5[0], sub_pk_anti_5[1], sub_pk_anti_5[2])
    # ax3.errorbar(sub_pk_noanti_5[0], sub_pk_noanti_5[1], sub_pk_noanti_5[2])
    #
    # plt.xlabel('Voltage vs reference (V)')
    # plt.ylabel('Current (mA)')
    # plt.xlim([-0.3, 0])
    # plt.ylim([-0.02, 0.01])
    # plt.legend(('BW25113 50$\mu g/ml$ Ampicillin', 'BW25133 00$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 50$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 0$\mu g/ml$ Ampicillin'),loc='lower right', fontsize = '10')
    # plt.title(r'Antibiotic Susceptibility of $10^{5}$ CFU/ml after 5 hours incubation')
    # #plt.savefig(os.path.join(directory,'susceptibility 10_5.png'), dpi=1200)
    #
    sub_bw_anti_6, bw_anti_6, leg= calculate_graph_data(paths[36:39])
    sub_bw_noanti_6, bw_noanti_6, leg = calculate_graph_data(paths[39:42])
    sub_pk_anti_6, pk_anti_6, leg = calculate_graph_data(paths[42:45])
    sub_pk_noanti_6, pk_noanti_6, leg = calculate_graph_data(paths[45:48])

    figure4 = plt.figure()
    ax4 = figure4.add_subplot(111)
    ax4.errorbar(sub_bw_anti_6[0], sub_bw_anti_6[1], sub_bw_anti_6[2])
    ax4.errorbar(sub_bw_noanti_6[0], sub_bw_noanti_6[1], sub_bw_noanti_6[2])
    ax4.errorbar(sub_pk_anti_6[0], sub_pk_anti_6[1], sub_pk_anti_6[2])
    ax4.errorbar(sub_pk_noanti_6[0], sub_pk_noanti_6[1], sub_pk_noanti_6[2])

    plt.xlabel('Voltage vs reference (V)')
    plt.ylabel('Current (mA)')
    plt.xlim([-0.3, 0])
    plt.ylim([-0.02, 0.01])
    plt.legend(('BW25113 50$\mu g/ml$ Ampicillin', 'BW25133 0$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 50$\mu g/ml$ Ampicillin', 'BW25113 with PKD3 0$\mu g/ml$ Ampicillin'),loc='lower right', fontsize = '10')
    plt.title(r'Antibiotic Susceptibility of $10^{6}$ CFU/ml after 5 hours incubation')
    plt.savefig(os.path.join(directory,'susceptibility 10_6 300dpi.png'), dpi=300)
    
    


if __name__ == '__main__':
    main()