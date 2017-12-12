from EC_Lab_CVReader import CVReader, get_data_paths
from SPV_Reader import SPV_Reader
from EIS_Reader import EISReader
import matplotlib.pyplot as plt
import numpy as np
import itertools
import scipy.stats as sts
def num_sort(name, split_loc):
    filename = name.split('\\')[-1]
    num = filename.split('_')[split_loc]
    return num


cv_directory = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\CV\\MB 14DF Grating\\Methylene Blue'
eis_directory = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\EIS'
mb_file = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\SPV\\Methylene Blue\\100uM MB 100mM PB square wave 2mv step 50mV 80hz_C01.mpt'
pb_spv_directory = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\SPV\\Square Wave Loop\\Phosphate Buffer'
mb_spv_directory = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\SPV\\Square Wave Loop\\Methylene Blue'

diaz_eis_directory = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\Diazonium 3\\EIS'
diaz_cv_directory = 'E:\\Chrome Download\\2min etch\\2min etch\\Electrochemistry\\Diazonium 3\\CV'

cv_paths = get_data_paths(cv_directory)
eis_paths = get_data_paths(eis_directory)

pb_spv_paths = get_data_paths(pb_spv_directory)
mb_spv_paths = get_data_paths(mb_spv_directory)

diaz_cv_paths = get_data_paths(diaz_cv_directory)
diaz_eis_paths = get_data_paths(diaz_eis_directory)

eis_paths.sort(key= lambda name: num_sort(name, 0))
cv_paths.sort(key= lambda name: num_sort(name,1))
eis_legends = ['100 mM', '10 mM', '1 mM', '100 $\mu$M', '10 $\mu$M', '1 $\mu$M']
fig, ax2 = plt.subplots()
fig2, ax = plt.subplots()
fig3, ax4 = plt.subplots()
ax3 = ax2.twinx()

fig4, (ax5, ax6) = plt.subplots(1,2)
ax7 = ax6.twinx()


fig5, ax8 = plt.subplots()

for eis_path in eis_paths[1:]:
    eis_reader = EISReader(eis_path, set_cycle=2)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')
scan_rates = list()
for cv_path in cv_paths:
    cv_reader = CVReader(cv_path, set_cycle=2)
    ax.plot(cv_reader.voltage, cv_reader.current)
    scan_rates.append(str(cv_reader.scan_rate) + ' mV/s')

diaz_leg = 1
diaz_leg_list = list()
for cv_path, eis_path in zip(diaz_cv_paths, diaz_eis_paths):
    diaz_leg_list.append(diaz_leg)
    diaz_leg +=1
    cv_reader = CVReader(cv_path)
    eis_reader = EISReader(eis_path)
    ax5.plot(cv_reader.voltage, cv_reader.current)
    ax6.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax7.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')

ax5.legend(diaz_leg_list, loc='lower right')
ax5.set_xlabel('Voltage (V vs Ag/AgCl)')
ax5.set_ylabel('Current (mA)')
ax6.set_xlabel('Frequency (Hz)')
ax6.set_ylabel('Magnitude ($\Omega$)')
ax7.set_ylabel('Phase (Degrees)')
fig4.tight_layout()

pb_current = list()
mb_current = list()
mb_max_voltage = list()
spv_voltage =0
for pb_file, mb_file in zip(pb_spv_paths, mb_spv_paths):
    spv_reader_pb = SPV_Reader(pb_file)
    spv_reader_mb = SPV_Reader(mb_file)
    pb_current.append(spv_reader_pb.current)
    mb_current.append(spv_reader_mb.current)
    mb_line_fit_c = list(itertools.chain(spv_reader_mb.current[:10], spv_reader_mb.current[-10:]))
    mb_line_fit_v = list(itertools.chain(spv_reader_mb.voltage[:10], spv_reader_mb.voltage[-10:]))
    mb_slope, mb_intercept, r, p, std = sts.linregress(mb_line_fit_v, mb_line_fit_c)
    mb_lin_fit = [mb_slope * x + mb_intercept for x in spv_reader_mb.voltage]
    mb_sub = np.asarray(spv_reader_mb.current) - np.asarray(mb_lin_fit)
    mb_max_voltage.append(spv_reader_mb.voltage[np.argmax(mb_sub)])
    spv_voltage_pb = spv_reader_pb.voltage
    spv_voltage_mb = spv_reader_mb.voltage

pb_current_mean = np.mean(pb_current, axis=0)
mb_current_mean = np.mean(mb_current, axis=0)
pb_current_std = np.std(pb_current, axis=0)
mb_current_std = np.std(mb_current, axis=0)

pb_current_start = pb_current_mean[:10]
pb_current_end = pb_current_mean[-10:]



pb_current_line_fit = list(itertools.chain(pb_current_mean[:10], pb_current_mean[-10:]))
pb_voltage_line_fit = list(itertools.chain(spv_voltage_pb[:10], spv_voltage_pb[-10:]))

mb_current_line_fit = list(itertools.chain(mb_current_mean[:10], mb_current_mean[-10:]))
mb_voltage_line_fit = list(itertools.chain(spv_voltage_mb[:10], spv_voltage_mb[-10:]))


pb_slope, pb_intercept, r, p , std = sts.linregress(pb_voltage_line_fit, pb_current_line_fit)
mb_slope, mb_intercept, r, p , std = sts.linregress(mb_voltage_line_fit, mb_current_line_fit)


pb_lin_fit = [pb_slope*x + pb_intercept for x in spv_voltage_pb]
mb_lin_fit = [mb_slope*x + mb_intercept for x in spv_voltage_mb]
pb_current_sub = pb_current_mean - pb_lin_fit
mb_current_sub = mb_current_mean - mb_lin_fit


ax4.errorbar(spv_voltage_mb, mb_current_sub, mb_current_std)
ax4.errorbar(spv_voltage_pb, pb_current_sub, pb_current_std)

ax4.legend([ '100mM PB 1mM MB', '100mM PB'])

ax4.set_xlabel('Voltage (V vs Ag/AgCl)')
ax4.set_ylabel('$\Delta$I ($\mu$A)')
mb_max_voltage_mean = np.mean(mb_max_voltage)
mb_max_voltage_std = np.std(mb_max_voltage)

ax4.plot([mb_max_voltage_mean, mb_max_voltage_mean], [-0.1,0.25], color='k')
ax4.plot([mb_max_voltage_mean - mb_max_voltage_std, mb_max_voltage_mean - mb_max_voltage_std], [-0.10,0.25], color='k', linestyle='--')
ax4.plot([mb_max_voltage_mean + mb_max_voltage_std, mb_max_voltage_mean + mb_max_voltage_std], [-0.1,0.25], color='k', linestyle='--')
print(mb_max_voltage_std)
ax4.set_ylim([-0.05,0.25])
ax4.set_xlim([-0.4,0.1])

ax8.hist(mb_max_voltage)



ax.set_xlabel('Voltage (V vs Ag/AgCl)')
ax.set_ylabel('Current (mA)')
ax.legend(scan_rates, loc=9, bbox_to_anchor=(1.1, 0.7))
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude ($\Omega$)')
ax2.legend(eis_legends, loc=9, bbox_to_anchor=(1.2, 0.7))
ax3.set_ylabel('Phase (Degrees)')
fig.subplots_adjust(wspace = 0.3, left= 0.1)
#fig.set_size_inches(18.5, 10.5)
plt.show()
