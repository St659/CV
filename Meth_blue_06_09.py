import os
import codecs
import numpy as np
import matplotlib.pyplot as plt



def get_cv_data(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        file_lines = file.readlines()

        header_line = get_header_line_number(file_lines)
        current_forward= list()
        reverse=list()
        voltage_reverse=list()
        forward = list()
        for line in file_lines[header_line:]:
            sl = line.split()

            if int(float(sl[1])) == 1:
                forward.append([float(sl[7]), float(sl[8])])
                current_forward.append(float(sl[8]))
            elif int(float(sl[1])) == 0:
                reverse.append([float(sl[7]), float(sl[8])])

        forward.sort()
        reverse.sort()

        return forward, reverse


def get_header_line_number(file_lines):
    for file in file_lines:
        if 'Nb header' in file:
            header_string = str(file)
            split_header_string =header_string.split()
            return int(split_header_string[-1])


def calculate_graph_data(*args):
    forward_list = list()
    reverse_list = list()
    forward_current_list = list()
    reverse_current_list = list()
    subtracted_reverse_current_list = list()
    subtracted_forward_current_list = list()
    data_files= args[0]

    if not isinstance(data_files, list):
        forward,reverse = get_cv_data(data_files)
        forward_list.append(forward)
        reverse_list.append(reverse)
    else:
        for data_file in data_files:
            forward,reverse = get_cv_data(data_file)
            forward_list.append(forward)
            reverse_list.append(reverse)

    voltage_forward = np.linspace(forward_list[0][0][0], forward_list[0][-1][0],500)
    voltage_reverse = np.linspace(reverse_list[0][0][0], reverse_list[0][-1][0],500)
    for data in forward_list:
        voltage_temp = list()
        current_temp = list()
        for x in data:
            voltage_temp.append(x[0])
            current_temp.append(x[1])
        interp_currents = np.interp(voltage_forward,voltage_temp, current_temp)

        non_faradaic = np.interp(0,voltage_temp, current_temp)
        forward_current_list.append(interp_currents)
        subtracted_forward_current_list.append(np.subtract(interp_currents,non_faradaic))

    for data in reverse_list:
        voltage_temp = list()
        current_temp = list()
        for x in data:
            voltage_temp.append(x[0])
            current_temp.append(x[1])
        interp_currents = np.interp(voltage_reverse,voltage_temp, current_temp)
        non_faradaic = np.interp(0,voltage_temp, current_temp)
        reverse_current_list.append(interp_currents)
        subtracted_reverse_current_list.append(np.subtract(interp_currents,non_faradaic))

    forward_current = np.array(forward_current_list)
    reverse_current = np.array(reverse_current_list)
    
    sub_forward_current = np.array(subtracted_forward_current_list)
    sub_reverse_current = np.array(subtracted_reverse_current_list)
    #
    forward_current_mean = np.mean(forward_current, axis=0)
    forward_current_std = np.std(forward_current, axis=0)
    reverse_current_mean = np.mean(reverse_current, axis=0)
    reverse_current_std = np.std(reverse_current, axis=0)
    
    sub_forward_current_mean = np.mean(sub_forward_current, axis=0)
    sub_forward_current_std = np.std(sub_forward_current, axis=0)
    sub_reverse_current_mean = np.mean(sub_reverse_current, axis=0)
    sub_reverse_current_std = np.std(sub_reverse_current, axis=0)

    current_mean = np.concatenate((forward_current_mean,reverse_current_mean[::-1]), axis=0)
    current_std = np.concatenate((forward_current_std, reverse_current_std[::-1]), axis=0)
    
    sub_current_mean = np.concatenate((sub_forward_current_mean,sub_reverse_current_mean[::-1]), axis=0)
    sub_current_std = np.concatenate((sub_forward_current_std, sub_reverse_current_std[::-1]), axis=0)
    voltage = np.concatenate((voltage_forward, voltage_reverse[::-1]), axis=0)

    file_path_split= data_files[0].split('/')
    legend_split = file_path_split[-1].split('_')
    legend = legend_split
    voltage_max_arg = np.argmax(forward_current_mean)
    voltage_max = np.argmax(voltage_max_arg)


    return [voltage, sub_current_mean, sub_current_std], [voltage, current_mean, current_std],legend

def get_data_paths(directory):
    filenames = os.listdir(directory)
    print(filenames)
    paths = list()
    for name in filenames:
        if '.mpt' in name:
            new_name = os.path.join(directory, name)
            paths.append(new_name)

    print(paths)
    return paths


def main():
    directory = "/Users/st659/Google Drive/Meth Blue 08-09"

    paths = get_data_paths(directory)
    sub_anti_100, anti_100 = calculate_graph_data(paths[:3])
    sub_blank_100, blank_100 = calculate_graph_data(paths[3:6])
    sub_no_anti_100, no_anti_100= calculate_graph_data(paths[6:9])

    sub_anti_10, anti_10 = calculate_graph_data(paths[9:12])
    sub_blank_10, blank_10 = calculate_graph_data(paths[12:15])
    sub_no_anti_10, no_anti_10 = calculate_graph_data(paths[15:18])

    sub_anti_50, anti_50 = calculate_graph_data(paths[18:21])
    sub_blank_50, blank_50= calculate_graph_data(paths[21:24])
    sub_no_anti_50, no_anti_50 = calculate_graph_data(paths[24:27])

    print("10 Graph")
    print("Max Current Anti: " + str(np.amax(anti_10[1])) + " Voltage: " + str(anti_10[0][np.argmax(anti_10[1])]))
    print("Max Current Blank: " + str(np.amax(blank_10[1])) + " Voltage: " + str(blank_10[0][np.argmax(blank_10[1])]))
    print("Max Current No Anti: " + str(np.amax(no_anti_10[1])) + " Voltage: " + str(no_anti_10[0][np.argmax(no_anti_10[1])]))

    print("50 Graph")
    print("Max Current Anti: " + str(np.amax(anti_50[1])) + " Voltage: " + str(anti_50[0][np.argmax(anti_50[1])]))
    print("Max Current Blank: " + str(np.amax(blank_50[1])) + " Voltage: " + str(blank_50[0][np.argmax(blank_50[1])]))
    print("Max Current No Anti: " + str(np.amax(no_anti_50[1])) + " Voltage: " + str(no_anti_50[0][np.argmax(no_anti_50[1])]))

    print("100 Graph")
    print("Max Current Anti: " + str(np.amax(anti_100[1])) + " Voltage: " + str(anti_100[0][np.argmax(anti_100[1])]))
    print("Max Current Blank: " + str(np.amax(blank_100[1])) + " Voltage: " + str(blank_100[0][np.argmax(blank_100[1])]))
    print("Max Current No Anti: " + str(np.amax(no_anti_100[1])) + " Voltage: " + str(no_anti_100[0][np.argmax(no_anti_100[1])]))


    # print(bw_mean)
    # print(bw_anti_mean)
    #

    figure1 = plt.figure()
    ax1 = figure1.add_subplot(111)
    ax1.errorbar(sub_blank_100[0], sub_blank_100[1], sub_blank_100[2])
    ax1.errorbar(sub_no_anti_100[0], sub_no_anti_100[1], sub_no_anti_100[2])
    ax1.errorbar(sub_anti_100[0], sub_anti_100[1], sub_anti_100[2])
    plt.xlabel('Voltage vs reference (V)')
    plt.ylabel('Current (mA)')
    plt.xlim([-0.3, 0])
    plt.ylim([-0.02, 0.01])
    plt.legend(('Blank', 'E.coli Without Antibiotics', 'E.coli With Antibiotics'),loc='lower right')
    plt.title(r'CV after 5 hours incubation with 100$\mu$M Methylene Blue')

    #plt.savefig(os.path.join(directory,'Meth_Blue_100_CV.png'), dpi=1200)

    figure2 = plt.figure()
    ax2 = figure2.add_subplot(111)
    ax2.errorbar(sub_blank_10[0], sub_blank_10[1], sub_blank_10[2])
    ax2.errorbar(sub_no_anti_10[0], sub_no_anti_10[1], sub_no_anti_10[2])
    ax2.errorbar(sub_anti_10[0], sub_anti_10[1], sub_anti_10[2])
    plt.xlim([-0.3, 0])
    plt.ylim([-0.015, 0.005])
    plt.xlabel('Voltage vs reference (V)')
    plt.ylabel('Current (mA)')
    plt.legend(('Blank', 'E.coli Without Antibiotics', 'E.coli With Antibiotics'), loc='lower right')
    plt.title(r'CV after 5 hours incubation with 10$\mu$M Methylene Blue')
    #plt.savefig(os.path.join(directory,'Meth_Blue_10_CV.png'), dpi=1200)


    figure3 = plt.figure()
    ax3 = figure3.add_subplot(111)
    ax3.errorbar(sub_blank_50[0], sub_blank_50[1], sub_blank_50[2])
    ax3.errorbar(sub_no_anti_50[0], sub_no_anti_50[1], sub_no_anti_50[2])
    ax3.errorbar(sub_anti_50[0], sub_anti_50[1], sub_anti_50[2])
    plt.xlabel('Voltage vs reference (V)')
    plt.ylabel('Current (mA)')
    plt.xlim([-0.3, 0])
    plt.ylim([-0.02, 0.005])
    plt.legend(('Blank', 'E.coli Without Antibiotics', 'E.coli With Antibiotics'),loc='lower right')
    plt.title(r'CV after 5 hours incubation with 50$\mu$M Methylene Blue')
    #plt.savefig(os.path.join(directory,'Meth_Blue_50_CV.png'), dpi=1200)

    # plt.errorbar(voltage, pkd_mean, pkd_err)
    # plt.errorbar(voltage, pkd_anti_mean, pkd_anti_err)
    plt.show()

if __name__ == "__main__":
    main()