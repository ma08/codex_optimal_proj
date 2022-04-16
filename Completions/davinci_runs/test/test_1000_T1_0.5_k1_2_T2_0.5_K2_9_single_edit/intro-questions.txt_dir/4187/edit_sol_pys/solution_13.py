
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)
print(a.reshape(3,2))
print(a.reshape(1,6))
print(a.reshape(6,1))
print(a.reshape(6))
print(a.reshape(-1))
