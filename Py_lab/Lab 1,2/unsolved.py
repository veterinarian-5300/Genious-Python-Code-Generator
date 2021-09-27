import matplotlib.pyplot as plt
import numpy as np
#t = [i for i in range (-10,20)]
t=np.linspace(-10, 10, 20)
plt.figure()
plt.subplot(221)
y = t*(t<=10)
plt.plot(t,y,color='red',linewidth=4)
plt.grid()
plt.title('y1=x')
plt.subplot(222)
y = (t*2)*[t<=10]
plt.plot(t,y,color='blue',linewidth=4)
plt.grid()
plt.title('y1=x^2')
plt.subplot(223)
y = (t*3)*[t<=10]
plt.plot(t,y,color='green',linewidth=4)
plt.grid()
plt.title('y1=x^3')
plt.subplot(224)
y = (t*4)*[t<=10]
plt.plot(t,y,color='black',linewidth=4)
plt.grid()
plt.title('y1=x^4')
plt.show()