import numpy as np
bonus = np.array([5, 0, 3, 10])
curved = np.minimum(scores + bonus, 100)
print(curved)