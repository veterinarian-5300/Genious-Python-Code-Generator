import numpy as np
A=np.array(
    [
        [1,2], 
        [3,5]
    ]
)
B=np.array([1,2])
result=np.linalg.solve(A, B)
print(result)