import numpy as np
matrix = np.array(
    [
        [1,2,3], 
        [3,2,6], 
        [3,5,7], 
        [45,7,8]
    ]
)
reshaped=matrix.reshape(12)
print(reshaped)