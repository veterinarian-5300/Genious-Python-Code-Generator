import matplotlib.pyplot as plt
import numpy as np
#t = [i for i in range (-10,20)]
t=np.linspace(-10, 10, 20)
plt.figure()
plt.subplot(211)
y = 1*(t>=-3)
y2 = 1*(t>=4)
out= y-y2
plt.plot(t,out,color='red',linewidth=4)
plt.grid()
plt.title('rectangle')

n= np.linspace(-5,20,20)
plt.subplot(212)
y = n*(n>=-5)
plt.plot(n,y,color='blue',linewidth=4)
plt.grid()
plt.title('ramp')

plt.tight_layout()
plt.show()
