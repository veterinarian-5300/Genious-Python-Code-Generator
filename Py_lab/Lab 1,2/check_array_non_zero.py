import numpy as np
matrix = np.array(
    [
        [1,2,3], 
        [3,2,6], 
        [3,0,7], 
        [45,7,8]
    ]
)

result = np.all((matrix != 0))
if result:
    print('Matrix contains all non-zero elements')
else:
    print('Matrix contains zeros as elements')