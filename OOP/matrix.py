import numpy as np
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

print(A + B)

print("*****************")
print(2 * A)
print("*****************")
print(A.T)
print("*****************")
print(A.dot(B))
print("*****************")
print(np.linalg.det(A))
print("*****************")
print(np.linalg.inv(A)) 