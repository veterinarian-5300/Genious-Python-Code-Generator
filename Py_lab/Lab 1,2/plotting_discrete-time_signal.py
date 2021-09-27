### importing libraries
import matplotlib.pyplot as plt

import numpy as np
## setting the x - coordinates
n = np.linspace(0.1, 14, 15)
# calculating corresponding the y - coordinates
xn = (np.sin(2*n*(np.pi)/15))
# plotting the points
plt.stem(n, xn, use_line_collection = True)
# naming the x axis
plt.xlabel('n (samples)')
# naming the y axis
plt.ylabel('x[n]')
# giving a title to my graph
plt.title('DT Sine curve')
#showing the plot
plt.show()