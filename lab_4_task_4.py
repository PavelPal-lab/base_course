import numpy as np

def func(a, b, N):

  x = np.linspace(a, b, N)
  y = x**2
  return y

a = float(input("начальная точка промежутка: "))
b = float(input("конечная точка промежутка: "))
N = int(input("количество точек: "))

y = func(a, b, N)
print(f"y = x^2 [{a}, {b}] в {N} точках:")
print(y)
