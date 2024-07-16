import matplotlib.pyplot as plt
import numpy as np

def plot_ellipse(a, b, x_min, x_max, N):
  x = np.linspace(x_min, x_max, N)
  y_top = np.sqrt(b*2 * (1 - (x*2 / a*2)))
  y_bottom = -y_top
  plt.plot(x, y_top, 'r-', label='Верхняя половина')
  plt.plot(x, y_bottom, 'r-', label='Нижняя половина')
  plt.xlim(x_min, x_max)
  plt.ylim(-b, b)
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('График эллипса')
  plt.legend()
  plt.grid(True)
  plt.axis('equal')
  plt.savefig('fig_task_3.png')
  plt.show()

a = float(input("Введите большую полуось (a): "))
b = float(input("Введите малую полуось (b): "))
x_min = float(input("Введите минимальное значение X: "))
x_max = float(input("Введите максимальное значение X: "))
N = int(input("Введите количество точек (N): "))

plot_ellipse(a, b, x_min, x_max, N)
