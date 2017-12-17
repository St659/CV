from EIS_Reader import EISReader
from EC_Lab_CVReader import get_data_paths
from matplotlib import pyplot as plt

eis_directory = 'E:\\Chrome Download\\todays data\\todays data\\Sputtered ITO EIS'

eis_paths = get_data_paths(eis_directory)

fig, eis_plot_freq = plt.subplots()
eis_plot_phase = eis_plot_freq.twinx()

for path in eis_paths:
    reader = EISReader(path, set_cycle=2)
    eis_plot_freq.loglog(reader.eis.frequency, reader.eis.magnitude)
    eis_plot_phase.semilogx(reader.eis.frequency, reader.eis.phase, linestyle='--')
eis_plot_freq.set_xlabel('Frequency (Hz)')
eis_plot_freq.set_ylabel('Magnitude ($\Omega$)')
eis_plot_phase.set_ylabel('Phase (degrees)')
plt.show()

