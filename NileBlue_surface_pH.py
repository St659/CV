from SPV_Reader import SPV_Reader
from EC_Lab_CVReader import get_data_paths
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as sts
spv_directory = '/Users/st659/Google Drive/todays data/Nile blue surface ph'
spv_paths = get_data_paths(spv_directory)
print(spv_paths)

fig, spv_plot = plt.subplots()


for path in spv_paths:
    reader = SPV_Reader(path)

    slope, intercept, r, p, std = sts.linregress([reader.voltage[0], reader.voltage[-1]], [reader.current[0], reader.current[-1]])
    lin_fit = [slope * x + intercept for x in reader.voltage]
    sub = np.asarray(reader.current) - np.asarray(lin_fit)
    spv_plot.plot(reader.voltage, sub)
spv_plot.legend(['pH 6', 'pH 7', 'ph 8'])
spv_plot.set_xlabel('Voltage (V vs Ag/AgCl)')
spv_plot.set_ylabel('$\Delta$I ($\mu$A)')
plt.show()

