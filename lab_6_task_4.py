import numpy as np
import matplotlib.pyplot as plt

def logarithmic_spiral(b, phi_min, phi_max):
  phi = np.linspace(phi_min, phi_max, 500)
  r = np.exp(b * phi)
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  return x, y

def archimedean_spiral(k, phi_min, phi_max):
  phi = np.linspace(phi_min, phi_max, 500)
  r = k * phi
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  return x, y

def spiral_of_jesse(k, phi_min, phi_max):
  phi = np.linspace(phi_min, phi_max, 500)
  r = k / np.sqrt(phi)
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  return x, y

def rose(k, phi_min, phi_max):
  phi = np.linspace(phi_min, phi_max, 500)
  r = np.sin(k * phi)
  x = r * np.cos(phi)
  y = r * np.sin(phi)
  return x, y

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

x, y = logarithmic_spiral(0.2, 0, 8 * np.pi)
axes[0, 0].plot(x, y)
axes[0, 0].set_title('Логарифмическая спираль')

x, y = archimedean_spiral(1, 0, 8 * np.pi)
axes[0, 1].plot(x, y)
axes[0, 1].set_title('Архимедова спираль')

x, y = spiral_of_jesse(1, 0.01, 8 * np.pi)
axes[1, 0].plot(x, y)
axes[1, 0].set_title('Спираль "жезл"')

x, y = rose(3, 0, 2 * np.pi)
axes[1, 1].plot(x, y)
axes[1, 1].set_title('Роза (k = 3)')

x, y = rose(2.5, 0, 2 * np.pi)
axes[1, 1].plot(x, y, '--', color='red')
axes[1, 1].set_title('Роза (k = 2.5)')

for ax in axes.flatten():
  ax.set_aspect('equal')
  ax.set_xlabel('x')
  ax.set_ylabel('y')

plt.tight_layout()

plt.axis('equal')

plt.savefig('fig_task_4.png')
