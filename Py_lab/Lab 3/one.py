import matplotlib.pyplot as plt
import numpy as np

x1=([1.0, 2.0, 3.0])
x2=([0.0, 1.0, 0.5,1.0])

#function from numpy for DT convolution
convolution = np.convolve(x1,x2)

#plotting the convolved signal
plt.stem(convolution, use_line_collection = True)

# naming the x axis
plt.xlabel('n')

# naming the y axis
plt.ylabel('x1[n]*x2[n]')


# Title to plot
plt.title('DT Convolution (19102110)')
plt.show()