import numpy as np
data = np.array([[2, 9, 1], [7, 1, 8]])
print("Sum of all: ", data.sum())
print("Column means: ", data.mean(axis=0))
print("Row maximums: ", data.max(axis=1))
print("Argmax per row: ", data.argmax(axis=1))
print("Sorted rows: ",np.sort(data, axis=1))
print("Argsort rows: ", np.argsort(data, axis=1))