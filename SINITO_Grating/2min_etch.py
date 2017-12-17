from EC_Lab_CVReader import CVReader, get_data_paths
from SPV_Reader import SPV_Reader
from EIS_Reader import EISReader
import matplotlib.pyplot as plt
import numpy as np
def num_sort(name, split_loc):
    filename = name.split('\\')[-1]
    num = filename.split('_')[split_loc]
    return num

def num_sort_loop(name):
    loop = name.split('_')[-1]
    loop_only = loop.split('.')[0]
    num = loop_only[4:]
    print(num)
    return num

plt.style.use(['seaborn-white', 'seaborn-notebook'])

cv_directory = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/CV/MB 14DF Grating/Methylene Blue'
eis_directory = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/EIS'
mb_file = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/SPV/Methylene Blue/100uM MB 100mM PB square wave 2mv step 50mV 80hz_C01.mpt'
pb_spv_directory = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/SPV/Square Wave Loop/Phosphate Buffer'
mb_spv_directory = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/SPV/Square Wave Loop/Methylene Blue'

diaz_eis_directory = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/Diazonium 3/EIS'
diaz_cv_directory = '/Users/st659/Google Drive/SiN ITO Grating ITO Thickness Test/2min etch/Electrochemistry/Diazonium 3/CV'



cv_paths = get_data_paths(cv_directory)
eis_paths = get_data_paths(eis_directory)

pb_spv_paths = get_data_paths(pb_spv_directory)
mb_spv_paths = get_data_paths(mb_spv_directory)

diaz_cv_paths = get_data_paths(diaz_cv_directory)
diaz_eis_paths = get_data_paths(diaz_eis_directory)



eis_paths.sort(key= lambda name: num_sort(name, 0))
cv_paths.sort(key= lambda name: num_sort(name,1))

diaz_cv_paths.sort(key=num_sort_loop)
diaz_eis_paths.sort(key=num_sort_loop)
print(diaz_cv_paths)
eis_legends = ['100 mM', '10 mM', '1 mM', '100 $\mu$M', '10 $\mu$M', '1 $\mu$M']
fig, ax2 = plt.subplots()
fig2, ax = plt.subplots()
fig3, ax4 = plt.subplots()
ax3 = ax2.twinx()

fig4, (ax5, ax6) = plt.subplots(1,2)
ax7 = ax6.twinx()

for eis_path in eis_paths:
    eis_reader = EISReader(eis_path, set_cycle=2)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')
scan_rates = list()
for cv_path in cv_paths:
    cv_reader = CVReader(cv_path, set_cycle=2)
    ax.plot(cv_reader.voltage, cv_reader.current)
    scan_rates.append(str(cv_reader.scan_rate) + ' mV/s')

diaz_leg = 1
diaz_legend = list()
for cv_path, eis_path in zip(diaz_cv_paths, diaz_eis_paths):
    diaz_legend.append(diaz_leg)
    diaz_leg +=1
    cv_reader = CVReader(cv_path)
    eis_reader = EISReader(eis_path)
    ax5.plot(cv_reader.voltage, cv_reader.current)
    ax6.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax7.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')


ax5.set_xlabel('Voltage (V vs Ag/AgCl)')
ax5.legend(diaz_legend, loc='lower right')
ax5.set_ylabel('Current (mA)')
ax6.set_xlabel('Frequency (Hz)')
ax6.set_ylabel('Magnitude ($\Omega$)')
ax7.set_ylabel('Phase (Degrees)')
fig4.tight_layout()
pb_current = list()
mb_current = list()
spv_voltage =0
for pb_file, mb_file in zip(pb_spv_paths, mb_spv_paths):
    spv_reader_pb = SPV_Reader(pb_file)
    spv_reader_mb = SPV_Reader(mb_file)
    pb_current.append(spv_reader_pb.current)
    mb_current.append(spv_reader_mb.current)
    spv_voltage_pb = spv_reader_pb.voltage
    spv_voltage_mb = spv_reader_mb.voltage

pb_current_mean = np.mean(pb_current, axis=0)
mb_current_mean = np.mean(mb_current, axis=0)
pb_current_std = np.std(pb_current, axis=0)
mb_current_std = np.std(mb_current, axis=0)

ax4.errorbar(spv_voltage_pb, pb_current_mean, pb_current_std)
ax4.errorbar(spv_voltage_mb, mb_current_mean, mb_current_std)
ax4.set_xlabel('Voltage (V vs Ag/AgCl)')
ax4.set_ylabel('$\Delta$I ($\mu$A)')
ax4.legend(['100mM PB', '100mM PB 1mM MB'])


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
