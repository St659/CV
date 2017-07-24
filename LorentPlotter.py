import os
import codecs
import numpy as np
import matplotlib.pyplot as plt

def lorentz(x, xo):
    square = np.square(x-xo)
    square_gamma = 0.25
    return 0.5/(square_gamma + square)


time = np.arange(300, 700)

for t in time:
    wave.append(lorentz(t, 500))

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(time, wave)

plt.show()