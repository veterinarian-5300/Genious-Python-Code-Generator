from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
from scipy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt
import numpy as np

N = 32
t = np.arange(N)

x=np.sin(t)
sp = fftshift(fft(x))
freq = fftshift(fftfreq(N))

plt.figure(figsize=(6,8))
plt.subplot(211)
plt.grid()
plt.plot(t, x)

plt.xlabel('t')
plt.ylabel('sin(t)')

plt.subplot(212)
plt.grid()
plt.plot(freq, abs(sp)) 


plt.xlabel('k')
plt.ylabel('Magnitude Spectrum {|X[k]|}')
plt.show()