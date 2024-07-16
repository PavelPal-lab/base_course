import matplotlib.pyplot as plt
import numpy as np

def plot_ellipse(x_min, x_max, N, a, b):
  x = np.linspace(x_min, x_max, N)
  y_positive = np.sqrt(b*2 * (1 - (x*2 / a*2)))
  y_negative = -np.sqrt(b*2 * (1 - (x*2 / a*2)))
  plt.plot(x, y_positive, 'r-', label='Верхняя половина')
  plt.plot(x, y_negative, 'r-', label='Нижняя половина')
  plt.xlim(x_min, x_max)
  plt.ylim(-b, b)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('График эллипса')
  plt.legend()
  plt.grid(True)
  plt.axis('equal')
  plt.savefig('fig_task_3.png')

N = int(input("Введите количество точек (N): "))
x_min = float(input("Введите минимальное значение X: "))
x_max = float(input("Введите максимальное значение X: "))
a = float(input("Введите большую полуось (a): "))
b = float(input("Введите малую полуось (b): "))

plot_ellipse(x_min, x_max, N, a, b)
