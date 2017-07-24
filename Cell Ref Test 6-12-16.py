from Looped_CV_Data import plot_looped_data
import matplotlib.pyplot as plt
import numpy as np
import os
directory = '/Users/st659/Google Drive/Cell Chamber Ref Test 02-12-16'
directory2 = '/Users/st659/Google Drive/Cell 1 Reference Measurement'
voltage_list, current_list =plot_looped_data(directory)


max_current_list = list()
max_voltage_list = list()
for current, voltage in zip(current_list, voltage_list):
    max_current = max(current)
    max_current_arg = np.argmax(current)
    max_current_list.append(max_current)
    max_voltage_list.append(voltage[max_current_arg])

time_points = np.linspace(0,len(max_current_list)*10, num=len(max_current_list))
plt.style.use(['seaborn-white','seaborn-poster'])
fig = plt.figure()
ax = fig.add_subplot(111)
for volt, curr in zip(voltage_list, current_list):
    ax.plot(volt,curr)
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (mA)')
ax.set_title('Cyclic Voltammetry of On Chip Electrode Array of 100 $\mu$M Methylene Blue over 6 Hours', y=1.04)
#plt.savefig(os.path.join(directory,'CV On Chip MB 28-11-16 300dpi.png'), dpi=300)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax3 = ax2.twinx()


time= list()
for num in time_points:
    time.append(num)


ax2.plot(time, max_current_list, label='Current')

ax3.plot(time, max_voltage_list, color='r', label='Voltage')


average_voltage = np.full(( len(max_voltage_list),1),np.mean(max_voltage_list,axis=0))
std_dev_1 = np.full((len(max_voltage_list),1), np.mean(max_voltage_list,axis=0) + np.std(max_voltage_list,axis=0))
std_dev_2 = np.full((len(max_voltage_list),1), np.mean(max_voltage_list,axis=0) - np.std(max_voltage_list,axis=0))
print(len(average_voltage))
ax3.plot(time, average_voltage, color='g', linestyle='--')
ax3.plot(time, std_dev_1, color='k', linestyle='--')
ax3.plot(time, std_dev_2, color='k', linestyle='--')

print(np.mean(max_voltage_list,axis=0))
print(np.std(max_voltage_list,axis=0))
print(max_voltage_list)
ax2.set_title('Maximum Current and Corresponding Voltage of CV of 100 $\mu$M Methylene Blue over 6 Hours', y=1.04)
ax2.set_xlabel('Time (Mins)')
ax2.set_ylabel('Current (mA)')
ax3.set_ylabel('Voltage (V)')
ax2.legend(loc=(0.1,0.15))
ax3.legend(loc=(0.1,0.1))
#plt.savefig(os.path.join(directory,'Max current On Chip MB 28-11-16 300dpi.png'), dpi=300)
plt.show()