# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
# setting the x - coordinates
x = np.arange(0, 2*(np.pi)*5, 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)
# potting the points
plt.plot(x, y, label ='sin(x)')
# naming the x axis

# naming the y axis
plt.ylabel('y(x)=sin(x)')
# giving a title to my graph
plt.title('Sine curve')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.xlabel('x - axis')

plt.show()