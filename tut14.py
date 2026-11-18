import numpy as np
m = np.array([[1,2,3],[4,5,6]])
row = np.array([10, 20, 30])
col = np.array([[100],[200]])
print(m + row)
print(m + col)
a = np.array([1, 2, 3])
b = np.array([10, 20])
diff = a[:, np.newaxis] - b[np.newaxis,:]
print(diff.shape)
print(diff)