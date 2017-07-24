from EC_Lab_CVReader import get_data_paths, CVReader
import matplotlib.pyplot as plt
import os

noapp_directory = 'E:\\Chrome Download\\Ferrocene\\No App'
app_directory = 'E:\\Chrome Download\\Ferrocene\\AppCV'

bare = get_data_paths(noapp_directory)
app =get_data_paths(app_directory)


figure = plt.figure()
ax = figure.add_subplot(111)
for path in app:
    reader = CVReader(path)
    ax.plot(reader.voltage, reader.current)
plt.legend(['Bare', 'Structured'])
ax.set_xlabel('Voltage (V vs Ag/AgCl)')
ax.set_ylabel('Current (mA)')
#plt.savefig(os.path.join(noapp_directory,'raw__bare_cv.png'), dpi=300)
plt.show()