from EC_Lab_CVReader import get_data_paths, CVReader
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sci
import os

bare_directory = 'E:\\Chrome Download\\Ferrocene\\App Struc'

bare = get_data_paths(bare_directory)

reader = CVReader(bare[-1])
#
figure = plt.figure()
figure2 = plt.figure()
# #
ax = figure.add_subplot(111)
ax2 = figure2.add_subplot(111)

rates = [30,60,100,200,400,700,1000]

forward_peak_voltage = list()
reverse_peak_voltage = list()
fwhm = list()
for rate in rates:
    forward_peak_voltage.append(list())
    reverse_peak_voltage.append(list())
    fwhm.append(list())

for path in bare:
        print(path)
        reader = CVReader(path)

        for i, r in enumerate(rates):
            if reader.scan_rate == r:
                forward_peak_voltage[i].append(reader.peak_forward_voltage)
                reverse_peak_voltage[i].append(reader.peak_reverse_voltage)
                fwhm[i].append((reader.fwhm[1] - reader.fwhm[0])*1000)

fwhm_mean = np.mean(fwhm, axis =1)
fwhm_std = np.std(fwhm, axis =1)
mean_forward = np.mean(forward_peak_voltage, axis = 1)
mean_reverse = np.mean(reverse_peak_voltage, axis = 1)
std_forward = np.std(forward_peak_voltage, axis = 1)
std_reverse = np.std(reverse_peak_voltage, axis = 1)

m_f, c_f, r_value, p_value, std_err = sci.linregress(np.log10(rates[2:]),mean_forward[2:])
m_r, c_r, r_value, p_value, std_err = sci.linregress(np.log10(rates[2:]),mean_reverse[2:])

print(m_f)
print(m_r)
print(c_f)
print(c_r)

x = np.linspace(10, rates[-1])



ax.errorbar(rates,mean_forward,std_forward, fmt= 'o')
ax.errorbar(rates,mean_reverse,std_reverse, fmt= 'o')
ax.legend(['Forward', 'Reverse'])
ax.plot(x, np.log10(x) * m_f + c_f, '--', color='k')
ax.plot(x, np.log10(x) * m_r + c_r, '--', color='k')
ax.set_xlabel('Scan Rate (mv/s)')
ax.set_ylabel('Peak Current Voltage (V)')
ax.set_xscale('log')
ax2.errorbar(rates, fwhm_mean, fwhm_std, fmt='o')
ax2.set_xscale('log')
ax2.set_ylabel('FWHM (mV)')
ax2.set_xlabel('log(Scan Rate) (mV)')
#ax.axvspan(reader.fwhm[0], reader.fwhm[1], facecolor='g', alpha=0.5)
fwhm = reader.fwhm[1] - reader.fwhm[0]
print(fwhm*1000)
#plt.savefig(os.path.join(bare_directory,'aperture struc fwhm plot.png'), dpi=300)
plt.show()
