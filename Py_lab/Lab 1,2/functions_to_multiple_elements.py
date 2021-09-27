import numpy as np
matrix = np.array(
    [
        [1,2,3], 
        [3,2,6], 
        [3,5,7], 
        [45,7,8]
    ]
)

add_1000 = lambda i:i +1000
vectorized_add_1000 = np.vectorize(add_1000)
print(vectorized_add_1000(matrix))
