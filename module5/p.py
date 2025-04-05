import numpy as np

a = np.random.randint(0, 21, (3, 3))
b = np.random.randint(0, 21, (3, 3))

addition = a + b
multiplication = np.dot(a, b)
transpose = multiplication.T

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Addition:\n", addition)
print("Multiplication:\n", multiplication)
print("Transpose of Product:\n", transpose)
