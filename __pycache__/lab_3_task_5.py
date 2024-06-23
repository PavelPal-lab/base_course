import numpy as np

N = int(input('N: '))
M = int(input('M: '))

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.sin(N * i + M * j + 1)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0

print(trigonometry_array)

trigonometry_array[:, [0, 1]] = trigonometry_array[:, [1, 0]]

print(trigonometry_array)
