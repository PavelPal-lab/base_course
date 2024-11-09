import numpy as np
import matplotlib.pyplot as plt

k = 0.08
V_0 = 1000

t = np.linspace (0, 4, 100)

V = V_0 * np.exp(-k * t)
V_4 = V_0 * np.exp(-k * 4)

print(f'изменение инвестиции: V(t) = {V_0} * exp(-{k} * 4) ')
print(f'за 4 года: {V_4:.2f} денежных единиц')

plt.plot(t, V)
plt.xlabel("время (годы)")
plt.ylabel("объем инвестиций")
plt.title("Изменение инвестиций")
plt.grid(True)
plt.savefig("изменение_инвестиций.png")
plt.show()
