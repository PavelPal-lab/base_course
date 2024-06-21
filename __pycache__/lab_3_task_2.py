import numpy as np
from lab_3_task_1 import g
h = 100
a = np.pi / 3
B = 30 / 180 * np.pi

v = np.sqrt ((g * h * np.tan(B) ** 2) / (2 * np.cos(a) ** 2 * (1 - np.tan(B) * np.tan(a))))
print(v)

T = 200
ε = 300
k = 1.380649 * 10 ** -23
e = 2,718281828459045235360
ℏ = 6.62607015 * 10 ** -34
