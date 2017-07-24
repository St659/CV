from EC_Lab_CVReader import get_data_paths, CVReader
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sci
import os

bare_directory = 'E:\\Chrome Download\\Ferrocene\\Bare'
struc_directory = 'E:\\Chrome Download\\Ferrocene\\Struc'

bare = get_data_paths(bare_directory)
struc = get_data_paths(struc_directory)
reader = CVReader(bare[-1])


figure2 = plt.figure()


ax2 = figure2.add_subplot(111)

rates = [30,60,100,200,400,700,1000]

for files in [bare, struc]:
    fwhm = list()
    for rate in rates:
        fwhm.append(list())
    for path in files:
        print(path)
        reader = CVReader(path)

        for i, r in enumerate(rates):
            if reader.scan_rate == r:
                fwhm[i].append((reader.fwhm[1] - reader.fwhm[0])*1000)

    fwhm_mean = np.mean(fwhm, axis =1)
    fwhm_std = np.std(fwhm, axis =1)
    ax2.errorbar(rates, fwhm_mean, fwhm_std, fmt='o')
ax2.legend(['Flat', 'Structured'],loc='Upper Left')
ax2.set_xscale('log')
ax2.set_ylabel('FWHM (mV)')
ax2.set_xlabel('log(Scan Rate) (mV)')
#ax.axvspan(reader.fwhm[0], reader.fwhm[1], facecolor='g', alpha=0.5)
fwhm = reader.fwhm[1] - reader.fwhm[0]
print(fwhm*1000)
plt.savefig(os.path.join(bare_directory,'no aperture fwhm plot.png'), dpi=300)
plt.show()