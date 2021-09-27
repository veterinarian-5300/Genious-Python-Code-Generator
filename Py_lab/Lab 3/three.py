import matplotlib.pyplot as plt
import numpy as np

x1=([-1.0, 2.0, -3.0])
x2=([0.0, -1.0, 0.5, 1.0])

n1=([-1,0,1])
n2=([-2,-1,0,1])

convolution =np.convolve(x1,x2 )
#Setting range of time axis

l1 = np.size(x1)
l2 = np.size(x2)
lconvolve=l1+l2-1

print('length of convolved signal=',lconvolve)
n=np.arange(n1[0]+n2[0],n1[-1]+n2[-1]+1,1)

print('n=',n)

# plotting the convolved signal

plt.stem(n,convolution, use_line_collection = True)

plt.title('DT Convolution (19102110)')
plt.show()