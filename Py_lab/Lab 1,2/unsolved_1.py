### importing libraries
import matplotlib.pyplot as plt

import numpy as np

t=np.linspace(-10, 10, 20)
# setting the x - coordinates
x = np.arange(0, 2*(np.pi)*5, 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)
# potting the points
plt.figure(figsize=(6, 6))
plt.subplot(311)
plt.plot(x, y, label ='sin(x)')


x1 = [1,2,3,4,5]
y1=np.exp(x1)
plt.subplot(312)
plt.plot(x1, y1, label ='negative exponential')

x2 = [1,2,3,4,5]
y2=np.sin(x2)+np.cos(x2)
plt.subplot(313)
plt.plot(x2, y2, label ='sin (x) + cos (x)')
 
plt.suptitle('Categorical Plotting')

plt.show()