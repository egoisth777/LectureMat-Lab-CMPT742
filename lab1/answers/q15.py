[](Project,%20Ray%20Marching%20SDFs.md)import random
import time
import numpy as np
from q6 import weighted_sum_2 as weighted_sum_list

random.seed(123)
c = time.time()
weights = [random.uniform(0, 1) for _ in range(1000000)]
values = [random.uniform(0, 1) for _ in range(1000000)]

print("Weighted sum lists:", weighted_sum_list(weights, values))
print()
print('time', time.time() - c)

c = time.time()
# Todo 1: Perform the weighted average using NumPy
weights = np.array(weights)
values = np.array(values)
total = np.inner(weights, values)
print(total)
print()
print('time', time.time() - c)
# Todo 2: Measure the time taken to perform the weighted average using NumPy vs list comprehension