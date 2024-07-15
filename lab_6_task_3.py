import matplotlib.pyplot as plt
import numpy as np

def elipce(minimum, maximum, N, a, b):
  
  x = (minimum, maximum, N)
  y = (minimum, maximum, N)

  X, Y = np.meshgrid(x, y)

  plt.savefig('fig_task_3.png')