import numpy as np
import matplotlib.pyplot as plt

m = 1
a_0 = 2
gamma = 0.5
v_0 = 0

t = np.linspace(0, 10, 100)

v = np.zeros_like(t)
v[0] = v_0
for i in range(len(t) - 1):
    v[i + 1] = v[i] + (a_0 - (gamma * v[i]**2 / m)) * (t[i + 1] - t[i])

plt.plot(t, v)
plt.xlabel("Время (с)")
plt.ylabel("Скорость (м/с)")
plt.title("Закон изменения скорости со временем")
plt.grid(True)
plt.savefig("изменение_скорости.png")
plt.show()
