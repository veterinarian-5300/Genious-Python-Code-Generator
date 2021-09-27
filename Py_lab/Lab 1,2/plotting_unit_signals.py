### importing libraries
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(-5, 5, 11)
delta = 1*(n==0)
u = 1*(n>=0)
plt.stem(n, delta, use_line_collection = True)

# naming the x axis
plt.xlabel('n')
plt.ylabel('x[n] = delta[n]')
# giving a title to my graph
plt.title('Unit Impulse Sequence')
plt.show()
plt.stem(n, u, use_line_collection = True)
plt.xlabel('n')
plt.ylabel('x[n] = u[n]')
# giving a title to my graph
plt.title('Unit Step Sequence')
# naming the y axis

# naming the x axis
# naming the y axis

plt.show()