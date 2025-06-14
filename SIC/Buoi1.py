import numpy as np

A = np.array([[2, 3], [5, 1]])
B = np.array([8, 7])  # Vector cột
X = np.linalg.solve(A, B)

print("Nghiệm là:")
print("x =", X[0])
print("y =", X[1])