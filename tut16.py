import numpy as np
v = np.arange(12)
print(v.reshape(3,4))
print(v.reshape(2, -1).shape)
print(v.reshape(3,4).T.shape)
print(v.reshape(3,4).flatten())

p = np.array([[1,2],[3,4]])
q = np.array([[5,6]])
print(np.vstack([p,q]))
print(np.concatenate([p,p],axis=1))

