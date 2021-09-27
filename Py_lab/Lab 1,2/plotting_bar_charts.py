### importing libraries
import matplotlib.pyplot as plt

import numpy as np

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 3))
plt.subplot(131)
#bar plot
plt.bar(names, values)
plt.subplot(132)
#scatter plot
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()



