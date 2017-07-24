from EC_Lab_CVReader import get_data_paths, CVReader
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sci
import os

bare_directory = 'E:\\Chrome Download\\Ferrocene\\Bare'
struc_directory = 'E:\\Chrome Download\\Ferrocene\\Struc'
app_directory = 'E:\\Chrome Download\\Ferrocene\\App'

bare = get_data_paths(bare_directory)
struc =get_data_paths(struc_directory)
app = get_data_paths(app_directory)



figure = plt.figure()
ax = figure.add_subplot(111)
#ax2 = figure.add_subplot(122)

rates = [30,60,100,200,400,700,1000]
fit = list()

for paths in [bare,struc]:
    peak = list()
    for rate in rates:
        peak.append(list())
    rate = list()
    fit_list = list()
    for path in paths:
        reader = CVReader(path)

        for i, r in enumerate(rates):
            if reader.scan_rate == r:
                peak[i].append(reader.peak_current)
        #peak.append(reader.peak_current)
        #rate.append(reader.scan_rate)


        #ax2.plot(reader.voltage, reader.current)
    mean_peak =np.mean(peak, axis=1)
    std_peak = np.std(peak, axis =1)

    m, c, r_value, p_value, std_err = sci.linregress(rates,mean_peak)
    fit.append([m,c])
    print(m)
    print(c)
    #hand = ax.errorbar(rates, mean_peak, std_peak, fmt= 'o' )
    ax.plot(reader.voltage, reader.current)
plt.legend(['Bare', 'Structured'])
#for f in fit:
#    x = np.linspace(0, rates[-1])
#    ax.plot(x, x * f[0] + f[1], '--', color='k')
ax.set_xlabel('Scan Rate (mV/s)')
ax.set_ylabel('Peak Current (mA)')
change = ((fit[1][0] - fit[0][0]) /fit[0][0])*100
print(change)
#plt.savefig(os.path.join(bare_directory,'flat results.png'), dpi=300)
plt.show()