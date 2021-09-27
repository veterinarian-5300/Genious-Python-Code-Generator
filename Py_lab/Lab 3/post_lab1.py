import matplotlib.pyplot as plt
import numpy as np

n=np.arange(0,4,1)
x1=1*(n>=0) - 1*(n>=3)
x2=1*(n>=0) - 1*(n>=2)

convolution = np.convolve(x1,x2)
plt.stem(convolution, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x1[n]*x2[n]')

plt.title('DT Convolution (19102110)')
plt.show()