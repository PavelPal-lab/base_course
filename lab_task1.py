import numpy as np
import matplotlib.pyplot as plt

N_0 = 100
k = 0.1
t_10 = np.log(10) / k

def бактерии(t):
    return N_0 * np.exp(k * t)

print("начальное количество бактерий:", N_0)
print("коэффицент размножения:", k)
print("время увелечения в 10 раз:", t_10)

t = np.linspace(0, t_10, 100)
N = бактерии(t)

plt.plot(t, N)
plt.xlabel("время")
plt.ylabel("количество бактерий")
plt.title("экспонциальный рост бактерий")
plt.grid(True)
plt.savefig("бактерии_график.png")
plt.show()
