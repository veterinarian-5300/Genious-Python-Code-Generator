import numpy as np
  

array1 = np.random.randint(10, size=(4, 3))
array2 = np.random.randint(10, size=(3, 5))
result = np.ones((4,5))

result = np.dot(array1, array2)


print('first_array\n',array1);
print('second_array\n',array2);
print('result_array\n',result);
