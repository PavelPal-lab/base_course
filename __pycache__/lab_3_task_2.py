import numpy as np
from lab_3_task_1 import g
h = 100
a = np.pi / 3
B = 30 / 180 * np.pi

v = np.sqrt ((g * h * np.tan(B) ** 2) / (2 * np.cos(a) ** 2 * (1 - np.tan(B) * np.tan(a))))
print(v)

from lab_3_task_1 import k
from lab_3_task_1 import e
from lab_3_task_1 import ℏ
T = 200
ε = 300

N = (2 / np.sqrt (np.pi)) * (ℏ / (k * T) ** 3 / 2) * e ** (-ε / k * T) * ε ** (T / 2)
print(N)
