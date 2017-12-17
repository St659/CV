from SPV_Reader import SPV_Reader
from EC_Lab_CVReader import get_data_paths,CVReader, cv_plot_labels
from matplotlib import pyplot as plt

plt.style.use(['seaborn-white', 'seaborn-notebook'])


spv_directory = '/Users/st659/Google Drive/Nile Blue/SPV'
cv_ph_directory = '/Users/st659/Google Drive/Nile Blue/CV/ph change'
cv_surface_directory = '/Users/st659/Google Drive/Nile Blue/CV/Sulfo NB'


spv_paths = get_data_paths(spv_directory)
cv_ph_paths = get_data_paths(cv_ph_directory)
cv_surface_paths = get_data_paths(cv_surface_directory)

fig, spv_plot = plt.subplots()
fig, cv_ph_plot = plt.subplots()
fig, cv_surface = plt.subplots()
for path in spv_paths[2:]:
    spv_reader = SPV_Reader(path)
    spv_plot.plot(spv_reader.voltage, spv_reader.normalised_current)

ph_voltage = list()
for path in cv_ph_paths:
    cv_reader = CVReader(path, set_cycle=2)
    cv_ph_plot.plot(cv_reader.voltage, cv_reader.current)
    ph_voltage.append((cv_reader.peak_forward_voltage))

cv_surface_max_voltage = list()
for path in cv_surface_paths:
    cv_reader = CVReader(path, set_cycle=2)
    cv_surface.plot(cv_reader.voltage, cv_reader.current)
    #cv_surface_max_voltage.append(cv_reader.peak_forward_voltage)

cv_plot_labels(cv_ph_plot)
cv_ph_plot.legend(['pH 6', 'pH 7', 'pH 8'])

#ph_plot.plot([6,7,8],ph_voltage,'o')
#ph_plot.set_xlim([5,9])
#cv_plot_labels(cv_ph_plot)
#cv_ph_plot.legend(['pH 6', 'pH 7', 'pH 8'])
spv_plot.set_xlabel('Voltage (V vs Ag/AgCl)')
spv_plot.set_ylabel('$\Delta$ Current ($\mu$A)')

plt.show()