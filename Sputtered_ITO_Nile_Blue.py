from EC_Lab_CVReader import CV_Plotter, get_data_paths
from SPV_Reader import SPV_Reader
import matplotlib.pyplot as plt

import os
plt.style.use(['seaborn-white', 'seaborn-notebook'])
ph6_directory = 'E:\\Chrome Download\\Surface Nile Blue\\ph6'
ph7_directory = 'E:\\Chrome Download\\Surface Nile Blue\\ph7'
ph8_directory = 'E:\\Chrome Download\\Surface Nile Blue\\ph8'

swv_directory = '/Users/st659/Google Drive/Sputtered ITO/Surface Nile Blue/SWV Plot'

# ph6_cv_plot = CV_Plotter(os.path.join(ph6_directory, 'CV'))
# ph7_cv_plot = CV_Plotter(os.path.join(ph7_directory, 'CV'))
# ph8_cv_plot = CV_Plotter(os.path.join(ph8_directory, 'CV'))

fig, spv_plot = plt.subplots()

print(get_data_paths(swv_directory))

for file in get_data_paths(swv_directory):
    spv_reader = SPV_Reader(file)
    spv_plot.plot(spv_reader.voltage, spv_reader.normalised_current)

spv_plot.legend(['pH 6', 'pH 7', 'pH 8'])
spv_plot.set_xlabel('Voltage vs Ag/AgCl (V)')
spv_plot.set_ylabel('$\Delta$ Current ($\mu$A)')


plt.show()