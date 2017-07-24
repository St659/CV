from EC_Lab_CVReader import get_data_paths, CVReader
from matplotlib import pyplot as plt
import scipy.stats as sci
import numpy as np
directory_pb = './Data/MB_PB'
directory_shu = './Data/MB_SHU'

pb_paths = get_data_paths(directory_pb)
shu_paths = get_data_paths(directory_shu)
pb_paths.sort()
shu_paths.sort()
plt.style.use(['seaborn-white', 'seaborn-notebook'])
figure = plt.figure()

ax = figure.add_subplot(121)
ax2 = figure.add_subplot(122)

figure2, (ax3, ax4)= plt.subplots(1,2, sharey=True)


rates = [20,50,100,250,500,1000,2500,5000]

forward_peak_voltage_pb = list()
reverse_peak_voltage_pb = list()

forward_peak_voltage_shu = list()
reverse_peak_voltage_shu = list()
for rate in rates:
    forward_peak_voltage_pb.append(list())
    reverse_peak_voltage_pb.append(list())
    forward_peak_voltage_shu.append(list())
    reverse_peak_voltage_shu.append(list())

for pb,shu in zip(pb_paths, shu_paths):


    reader_pb = CVReader(pb)
    reader_shu = CVReader(shu)

    reader_pb.get_max_voltages_between_limits(-0.37, 0)
    reader_shu.get_max_voltages_between_limits(-0.4, -0.02)
    for i, r in enumerate(rates):

        if reader_pb.scan_rate == r:
            forward_peak_voltage_pb[i].append(reader_pb.peak_forward_voltage)
            reverse_peak_voltage_pb[i].append(reader_pb.peak_reverse_voltage)
        if reader_shu.scan_rate == r:
            forward_peak_voltage_shu[i].append(reader_shu.peak_forward_voltage)
            reverse_peak_voltage_shu[i].append(reader_shu.peak_reverse_voltage)
    print(pb)
    print(shu)
    ax.plot(reader_shu.voltage, reader_shu.current)
    ax2.plot(reader_pb.voltage, reader_pb.current)
#plt.legend(['Bare', 'Structured'])
ax.set_xlabel('Voltage (V vs Ag/AgCl)')
ax2.set_xlabel('Voltage (V vs Ag/AgCl)')
ax.set_ylabel('Current (mA)')

ax3.semilogx(rates, forward_peak_voltage_pb ,'o')
ax3.semilogx(rates, reverse_peak_voltage_pb,'o')

ax4.semilogx(rates, forward_peak_voltage_shu, 'o')
print(forward_peak_voltage_pb[4:])
pb_forward = [item for sublist in forward_peak_voltage_pb for item in sublist]
pb_reverse = [item for sublist in reverse_peak_voltage_pb for item in sublist]
m_f, c_f, r_value, p_value, std_err = sci.linregress(np.log10(rates[4:]),pb_forward[4:])
m_r, c_r, r_value, p_value, std_err = sci.linregress(np.log10(rates[4:]),pb_reverse[4:])
x = np.linspace(10, rates[-1])

ax4.semilogx(rates, reverse_peak_voltage_shu, 'o')
ax3.plot(x, np.log10(x) * m_f + c_f, '--', color='k')
ax3.plot(x, np.log10(x) * m_r + c_r, '--', color='k')
ax4.legend(['Forward Voltage', 'Reverse Voltage'], prop={'size':8})
ax.legend(['20 mV/s','50 mV/s', '100 mV/s', '250 mV/s', '500 mV/s', '1000 mV/s', '2500 mV/s', '5000 mV/s'], prop={'size':8})
ax3.set_xlabel('Scan Rate (mV/s)')
ax3.set_ylabel('Voltage (V)')

ax4.set_xlabel('Scan Rate (mV/s)')

#plt.savefig(os.path.join(noapp_directory,'raw__bare_cv.png'), dpi=300)
plt.show()