# importing the module
import matplotlib.pyplot as plt
# x axis values
x = [1,2,3,4,5]
# corresponding y axis values
y = [2,4,1,3,5]
# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# Title to plot
plt.title('Plot')
# function to show the plot
plt.show()