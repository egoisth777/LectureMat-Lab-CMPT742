[](Project,%20Ray%20Marching%20SDFs.md)import numpy as np

# Todo 1: Create required numpy array
matrix = np.random.uniform(0, 1, (10, 10))
print(matrix.shape)
# Todo 2: Manipulate the array into desired format using array slicing
matrix[:, :] = 7
matrix[0:2, :] = 0
matrix[-2:, :] = 0
matrix[:, 0:2] = 0
matrix[:, -2:] = 0

print(matrix)