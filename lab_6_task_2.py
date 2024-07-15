import matplotlib.pyplot as plt
import numpy as np

def hyper(minimum, maximum, N):
  N = int(N/2)

  x = np.linspace(0, maximum, N+1)
  x = np.delete(x, 0)
  y = 20/x
  plt.plot(x, y, color='b', label='my hyperbola')

  x = np.linspace(minimum, 0, N+1)
  x = np.delete(x, -1)
  y = 20/x
  plt.plot(x, y, color='b')

  plt.xlabel('Coord - x')
  plt.ylabel('Coord - y')
  plt.title('Hyperbola')
  plt.grid()
  plt.legend()
  plt.axis('equal')
  plt.savefig('fig_task_2.png')

hyper(int(input('x_min: ')), int(input('x_max: ')), int(input('значение N: ')))