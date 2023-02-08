import numpy as np

# 1
theta = np.array([[1, -1, 2, -3]])

options = [
    np.array([[1, -1, 2, -3]]),
    np.array([[1, 2, 3, 4]]),
    np.array([[-1, -1, -1, -1]]),
    np.array([[1, 1, 1, 1]]),
]

positives = []
for idx, option in enumerate(options):
    if np.dot(theta, option.T,) > 0:
        positives.append(idx+1)
print(positives)
