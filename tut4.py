import numpy as np
x = np.array([1, 2, 3])
print(x.dtype)
y = np.array([1, 2, 3], dtype = float)
print(y.dtype, y)
z = np.array([1.7, 2.2, 3.9]) .astype(int)
print(z)
pixels = np.array([0, 128, 155] , dtype = np.uint8)
print(pixels.dtype, pixels.itemsize, "byte per value")