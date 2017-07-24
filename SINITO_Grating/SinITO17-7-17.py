from EC_Lab_CVReader import CVReader, get_data_paths
from EIS_Reader import EISReader
import matplotlib.pyplot as plt
cv_directory = 'E:\\Chrome Download\\SinITOGrating 17-7-17\\SinITOGrating 17-7-17\\CV'
eis_directory = 'E:\\Chrome Download\\SinITOGrating 17-7-17\\SinITOGrating 17-7-17\\EIS'

cv_paths = get_data_paths(cv_directory)
eis_paths = get_data_paths(eis_directory)
fig, (ax, ax2) = plt.subplots(1,2)
ax3 = ax2.twinx()

for cv_path, eis_path in zip(cv_paths,eis_paths):
    cv_reader = CVReader(cv_path, set_cycle=2)
    eis_reader = EISReader(eis_path, set_cycle=2)
    ax.plot(cv_reader.voltage, cv_reader.current)
    ax2.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
    ax3.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase, linestyle='--')

ax.set_xlabel('Voltage (V vs Ag/AgCl)')
ax.set_ylabel('Current (mA)')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude ($\Omega$)')
ax3.set_ylabel('Phase (Degrees)')
fig.subplots_adjust(wspace = 0.3)
plt.show()
