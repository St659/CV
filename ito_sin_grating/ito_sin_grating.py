from SPV_Reader import SPV_Reader
from EC_Lab_CVReader import CVReader,get_data_paths, cv_plot_labels
from EIS_Reader import EISReader
from matplotlib import pyplot as plt

plt.style.use(['seaborn-white', 'seaborn-notebook'])

#Electrochemical data from first deposited ITO SIN grating.
spv_directory = '/Users/st659/Google Drive/ito_sin_18_10_17/Electrochemistry/SPV'
eis_directory = '/Users/st659/Google Drive/ito_sin_18_10_17/Electrochemistry/EIS'
cv_directory = '/Users/st659/Google Drive/ito_sin_18_10_17/Electrochemistry/CV MB'

spv_paths = get_data_paths(spv_directory)
eis_paths = get_data_paths(eis_directory)
cv_paths = get_data_paths(cv_directory)

#Create plots
fig, spv_plot = plt.subplots()
fig2, eis_plot_mag = plt.subplots()
eis_plot_phase = eis_plot_mag.twinx()
fig3, cv_plot = plt.subplots()

# for path in spv_paths:
#     spv_reader = SPV_Reader(path)
#     spv_plot.plot(spv_reader.voltage, spv_reader.current)
spv_reader = SPV_Reader(spv_paths[1])
spv_plot.plot(spv_reader.voltage, spv_reader.current)


spv_plot.set_xlabel('Voltage (V vs Ag/AgCl)')
spv_plot.set_ylabel('$\Delta$ Current ($\mu$A)')
spv_plot.legend(['100mM PB','1mM MB 100mM PB'])

for path in eis_paths:
    eis_reader = EISReader(path)
    eis_plot_mag.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    eis_plot_phase.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')
eis_plot_mag.set_xlabel('Frequency (Hz)')
eis_plot_mag.set_ylabel('|Z| ($\Omega$)')
eis_plot_phase.set_ylabel('$\\angle$ ($\degree$)')

for path in cv_paths:
    cv_reader = CVReader(path, set_cycle=2)
    cv_plot.plot(cv_reader.voltage, cv_reader.current, label=str(cv_reader.scan_rate) + ' mV/s')

cv_plot_labels(cv_plot)
cv_plot.set_xlim([-0.4, 0.1])
cv_plot.legend(loc='upper left')


plt.show()
