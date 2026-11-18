import numpy as np
A = np.array([[1,3],[3,4]])
B = np.array([[5,6],[7,8]])
print(A*B)
print(A@B)
print(np.linalg.inv(A))
print(np.linalg.norm([3,4]))