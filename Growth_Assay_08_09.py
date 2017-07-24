import numpy as np
import matplotlib.pyplot as plt

anti_100 = [-0.013, 0.003, -0.001]
noanti_100 = [0.851,0.936,0.632]

anti_50 = [0.001,0.002,-0.004]
noanti_50 = [1.227,0.757,1.028]

anti_10= [-0.007, 0.005, 0.001]
noanti_10= [1.201,1.157,0.443]

anti_0 = [0.000, 0.011, 0.000]
noanti_0 = [1.08, 0.975, 1.411]


anti_100_mean = np.mean(anti_100)
noanti_100_mean = np.mean(noanti_100)
anti_100_std = np.std(anti_100)
noanti_100_std = np.std(noanti_100)

anti_50_mean = np.mean(anti_50)
noanti_50_mean = np.mean(noanti_50)
anti_50_std = np.std(anti_50)
noanti_50_std = np.std(noanti_50)

anti_10_mean = np.mean(anti_10)
noanti_10_mean = np.mean(noanti_10)
anti_10_std = np.std(anti_10)
noanti_10_std = np.std(noanti_10)

anti_0_mean = np.mean(anti_0)

noanti_0_mean = np.mean(noanti_0)
anti_0_std = np.std(anti_0)
noanti_0_std = np.std(noanti_0)

anti_mean = (anti_0_mean, anti_10_mean, anti_50_mean, anti_100_mean)
anti_std = (anti_0_std, anti_10_std, anti_50_std, anti_100_std)

print(len(anti_mean))

noanti_mean = [noanti_0_mean, noanti_10_mean, noanti_50_mean, noanti_100_mean]
noanti_std = [noanti_0_std, noanti_10_std, noanti_50_std, noanti_100_std]

fig, ax = plt.subplots()
rects1 = ax.bar(np.arange(4), anti_mean, 0.35, color='r', yerr=anti_std)
rects2 = ax.bar(np.arange(4) + 0.35, noanti_mean, 0.35, color='g', yerr=noanti_std)
ax.set_xticks(np.arange(4) +0.35)
ax.set_xticklabels(('0', '10', '50', '100'))
ax.legend((rects1[0], rects2[0]), ('Anti', 'No Anti'))
ax.set_ylabel('OD$_{600}$')
ax.set_xlabel('Methylene Blue Concentration $\mu g/ml$')
ax.set_title('Growth of BW25113 in Methylene Blue ')
ax.set_ylim([0, 1.4])

plt.show()