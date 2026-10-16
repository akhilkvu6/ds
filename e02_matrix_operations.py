# Exercise 2: Matrix Operations

# Question 1: Write a NumPy program to create two matrices (read values from user) and find the following: 1. Dot Product 2. Transpose 3. Trace 4. Rank 5. Determinant 6. Inverse 7. Eigen values and eigen vectors.

import numpy as np
from numpy import linalg

def matrixread(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            num = int(input("Enter element " + str(i) + "," + str(j) + ": "))
            row.append(num)

        matrix.append(row)

    return matrix


n = int(input("Enter the order of the matrix: "))

print("Enter Matrix 1")
matrix1 = np.array(matrixread(n))

print("Enter Matrix 2")
matrix2 = np.array(matrixread(n))

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

# 1. Dot Product
print("Dot Product:")
print(np.dot(matrix1, matrix2))

# 2. Transpose
print("Transpose of Matrix 1:")
print(np.transpose(matrix1))

# 3. Trace
print("Trace of Matrix 1:")
print(np.trace(matrix1))

# 4. Rank
print("Rank of Matrix 1:")
print(linalg.matrix_rank(matrix1))

# 5. Determinant
print("Determinant of Matrix 1:")
print(np.linalg.det(matrix1))

# 6. Inverse
if np.linalg.det(matrix1) != 0:
    print("Inverse of Matrix 1:")
    print(linalg.inv(matrix1))
else:
    print("Matrix 1 does not have an inverse.")

# 7. Eigen values and eigen vectors
eigenvalues, eigenvectors = linalg.eig(matrix1)

print("Eigen values:")
print(eigenvalues)

print("Eigen vectors:")
print(eigenvectors)