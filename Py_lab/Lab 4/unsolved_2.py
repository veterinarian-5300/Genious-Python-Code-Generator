import matplotlib.pyplot as plt
import numpy as np
import scipy.fft


n = np.linspace(0, 20, 21)
u1=2*(n>=0)
u2=4*(n>=2)
u3=2*(n>=6)

x1=(u1-u2+u3)
dft=scipy.fft.fft(x1)

plt.figure(figsize=(8,9))
plt.subplot(2,1,1)
plt.stem(dft.real, use_line_collection=True)

#naming the axis
plt.xlabel('n')
plt.ylabel('Real {x[n]}')

#plot title
plt.title('Real part of DFT')

#imaginary part
plt.subplot(2,1,2)
plt.stem(dft.imag,use_line_collection=True)

#naming the axis
plt.xlabel('n')
plt.ylabel('imag{x[n]}')

#plot title
plt.title('Imaginary part of DFT')

plt.show()
print('DFT x[n] =',dft)