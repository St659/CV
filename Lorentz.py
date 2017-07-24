import os
import codecs
import numpy as np
import matplotlib.pyplot as plt

def lorentz(x, xo):
    square = np.square(x-xo)
    square_gamma = 1
    return 1/(square_gamma + square)

wave = list()
wave2 = list()
time = np.arange(500, 700)

for t in time:
    wave.append(lorentz(t, 600))

for t in time:
    wave2.append(lorentz(t, 620))

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(time, wave)
#ax.plot(time, wave2)
ax.set_ylabel('Reflectance')
ax.set_xlabel('Wavelength (nm)')

directory = 'E:\\Git'

plt.savefig(os.path.join(directory,'photonic crystal.png'), dpi=300)

plt.show()