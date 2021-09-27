import matplotlib.pyplot as plt
# line 1 points
x1 = [1,2,3,4,5]
y1 = [2,4,1,3,5]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")
# line 2 points
x2 = [1,2,3,4,5]
y2 = [4,1,3,2,5]
# plotting the line 2 points

plt.plot(x2, y2, label = "line 2")
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same plot')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()