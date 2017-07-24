from Looped_CV_Data import plot_looped_data, get_maximum_current
from matplotlib import pyplot as plt

directory_list = ['/Users/st659/Google Drive/Large Ref 1 9-12-16',
             '/Users/st659/Google Drive/Large Ref 2 9-12-16']

plt.style.use(['seaborn-white','seaborn-poster'])
results = list()
max_results = list()
fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()
for directory in directory_list:
    voltage, current =plot_looped_data(directory)
    split_directory = directory.split(" ")
    voltage_max, current_max, time_points = get_maximum_current(voltage,current)
    ax.plot(time_points, voltage_max, label=split_directory[-1])
    ax2.plot(time_points,current_max, linestyle = '--')
ax.legend()
ax.set_title('Stability of Large Au Pseudo Reference over Time in 100 $\mu$M MB')
ax.set_ylabel('Voltage (V)')
ax2.set_ylabel('Current (mA)')
ax.set_xlabel('Time (mins)')
plt.show()

