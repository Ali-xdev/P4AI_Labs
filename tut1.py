import numpy as np
import time 
n = 1_000_000
numbers_list_ = list(range(n))
numbers_arr = np.arrange(n)

start = time.perf_counter()
squares_list = [x**2 for x in numbers_list_]
list_time = time.perf_counter() - start


start = time.perf_counter()
squares_arr = numbers_arr**2
arr_time = time.perf_counter() -start

print(f"list loop: { list_time * 1000:.1f} ms")
print(f"NumPY array: { arr_time * 1000:.1f} ms")
print(f"NumPY is about: { list_time / arr_time:.0f} x faster")