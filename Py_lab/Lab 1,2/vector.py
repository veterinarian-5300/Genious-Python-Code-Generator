# importing numpy
import numpy as np

# creating a 1-D list (Horizontal)
list1 = [4,45,34,33,2,2,1]

# creating a 1-D list (Vertical)
list2 = [[31],	[22],	[23]]

# vector as row
vector1 = np.array(list1)

# vector as column
vector2 = np.array(list2)

# showing horizontal vector
print("Horizontal Vector")
print(vector1)

print("----------------")

# showing vertical vector
print("Vertical Vector")
print(vector2)
