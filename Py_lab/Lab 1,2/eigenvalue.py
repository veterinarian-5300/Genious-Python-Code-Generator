import numpy as np
from numpy import linalg

A=np.array([[5,3],[-6,-4]])


w,v=np.linalg.eig(A)
print(w)
print(v)