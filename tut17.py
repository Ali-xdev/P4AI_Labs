import numpy as np
rng = np.random.default_rng(seed=0)
print(rng.random(3).round(3))
print(rng.integers(0, 10, size=5))
print(rng.normal(loc=50, scale=5, size=4).round(1))
print(rng.permutation(6))