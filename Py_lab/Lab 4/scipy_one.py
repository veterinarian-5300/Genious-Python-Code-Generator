import scipy.fft
import matplotlib.pyplot as plt
import numpy as np


x1=([0,4,2,0])
dft=scipy.fft.fft(x1)

plt.figure(figsize=(8,9))
plt.subplot(2, 1, 1)
plt.stem(dft.real, use_line_collection = True)

plt.xlabel('k')
plt.ylabel('Real{x[k]}')

plt.title('Real part of DFT')

plt.subplot(2, 1, 2)
plt.stem(dft.imag, use_line_collection = True)

plt.xlabel('k')
plt.ylabel('Img{X{k}}')

plt.title('Imaginary Part of DFT')

plt.show()
print('DFT X[k] =',dft)

