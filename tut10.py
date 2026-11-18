import numpy as np
ages = np.array([17, 22, 15, 30, 19, 41])
marks = ages >= 18
print(marks)
print(ages|marks)
print(ages[(ages>=18)&(ages<30)])
print("Number of adults:", marks.sum())