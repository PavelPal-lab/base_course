import matplotlib.pyplot as plt
import numpy as np

def ellipse(a, b, x_min, x_max, N):
  t = np.linspace (0, 2*np.pi, N)
  x = a * np.cos(t)
  y = b * np.sin(t)

  plt.plot(x, y)

  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('График эллипса')
  plt.grid(True)
  plt.axis('equal')
  plt.savefig('fig_task_3.png')

a = float(input("Введите большую полуось (a): "))
b = float(input("Введите малую полуось (b): "))
x_min = float(input("Введите минимальное значение X: "))
x_max = float(input("Введите максимальное значение X: "))
N = int(input("Введите количество точек (N): "))

ellipse(a, b, x_min, x_max, N)
