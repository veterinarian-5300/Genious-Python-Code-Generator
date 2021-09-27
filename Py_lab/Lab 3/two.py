import matplotlib.pyplot as plt
import numpy as np

x1=([-1.0, 2.0, -3.0])
x2=([0.0, -1.0, 0.5, 1.0])
convolution =np.convolve(x1,x2 )

#Setting range of time axis
l1 = np.size(x1)
l2 = np.size(x2)

n=np.arange(0,l1+l2-1,1)
print(l1+l2-1)

# plotting the convolved signal
plt.stem(n,convolution, use_line_collection = True)

# naming the x axis
plt.xlabel('n')

# naming the y axis
plt.ylabel('x1[n]*x2[n]')

# Title to plot
plt.title('DT Convolution (19102110)')
plt.show()