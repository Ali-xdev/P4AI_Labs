import numpy as np
a = np.array([4 ,48, 15, 16, 23, 42])           # 1D array
m = np.array([[1, 2, 3],[4, 5, 6]])             # 2D array
t = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]]) # 3D array

for name , x in [("a", a), ("M", m), ("t", t)]:
    print(f"{name}: ndim = {x.ndim} , hape = {x.shape}, size={x.size}, dtype = {x.dtype}")