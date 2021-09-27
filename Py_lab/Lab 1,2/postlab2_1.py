import matplotlib.pyplot as plt
import numpy as np
# setting the x - coordinates
x = np.linspace(0,5,500)
# setting the corresponding y - coordinates
plt.figure()
plt.subplot(311)
y = np.sin(20*x)
plt.plot(x, y, label ='sin(x)',color='blue',linewidth=4)
plt.legend()
plt.subplot(312)
y = np.exp(-x)
plt.plot(x, y, label ='exp(-x)',color='red',linewidth=4)
plt.legend()
plt.subplot(313)
y =  0.8*np.exp(-3*x)*np.sin(20*x)
# potting the points
plt.plot(x, y, label ='damped  sin(x)',color='green',linewidth=4)
# naming the x axis

# naming the y axis
plt.ylabel('y(x)=sin(x)')
plt.axis([0,5,-0.5,0.5])
# show a legend on the plot
plt.legend()
plt.tight_layout()

plt.show()
