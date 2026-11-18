import numpy as np
a = np.array([5, -3, 8, -1, 0, 7])
print(a[[0, 2, 5]])
print(np.where(a>0, "pos", "not"))
a[a < 0] = 0
print(a)