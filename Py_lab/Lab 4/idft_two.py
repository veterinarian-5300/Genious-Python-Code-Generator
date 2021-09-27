import matplotlib.pyplot as plt
import numpy as np
import scipy.fft

Xk=[6,-2-4j,-2,-2+4j]
idft=scipy.fft.ifft(Xk)

plt.figure(figsize=(8,9))
plt.subplot(2, 1, 1)
plt.stem(idft.real, use_line_collection = True)

plt.xlabel('n')
plt.ylabel('Real{x[n]}')

plt.title('Real part of IDFT')

plt.subplot(2, 1, 2)
plt.stem(idft.imag, use_line_collection = True)

plt.xlabel('n')
plt.ylabel('Img{x[n]}')

plt.title('Imaginary Part of IDFT')

plt.show()
print('IDFT x[n] =',idft)