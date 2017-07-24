from Looped_CV_Data import plot_looped_data
import matplotlib.pyplot as plt
import numpy as np
import os

ecoli = '/Users/st659/Google Drive/Ecoli 50uM MB 1-12-2016'
ref = '/Users/st659/Google Drive/Celll Ref Measurements 28-11-16'
ref_volt_list, ref_current_list =plot_looped_data(ref)
ecoli_volt_list, ecoli_current_list = plot_looped_data(ecoli)


max_current_ref_list = list()
max_voltage_ref_list = list()
max_current_ecoli_list = list()
max_voltage_ecoli_list = list()
for current, voltage in zip(ref_current_list, ref_volt_list):
    max_current = max(current)
    max_current_arg = np.argmax(current)
    max_current_ref_list.append(max_current)
    max_voltage_ref_list.append(voltage[max_current_arg])
    
for current, voltage in zip(ecoli_current_list, ecoli_volt_list):
    max_current = max(current)
    max_current_arg = np.argmax(current)
    max_current_ecoli_list.append(max_current)
    max_voltage_ecoli_list.append(voltage[max_current_arg])

print(max_voltage_ref_list)
print(len(max_voltage_ref_list))

normal_ecoli_voltage = list()
normal_ref_voltage = list()
time_points_ec = np.linspace(0,len(max_current_ecoli_list)*10, num=len(max_current_ecoli_list))
times_points_ref = np.linspace(0,len(max_current_ref_list)*10, num=len(max_current_ref_list))
time = list()
max_voltage_ref_list.pop(0)
max_voltage_ref_list.pop(-2)
for num in times_points_ref:
    time.append(num)
time.pop(0)
time.pop(-2)
for voltage in max_voltage_ecoli_list:
    normal_ecoli_voltage.append(voltage - max_voltage_ecoli_list[0])
    
for voltage in max_voltage_ref_list:
    normal_ref_voltage.append(voltage - max_voltage_ref_list[0])




fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(time_points_ec, normal_ecoli_voltage)
ax.plot(time, normal_ref_voltage)
plt.show()