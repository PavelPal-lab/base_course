import numpy as np

def E(m, h, v):
  
  g = 9.81
  Ep = m * g * h
  Ek = (m * v**2) / 2
  E = Ep + Ek
  return E

m = int(input("Введите массу тела: "))
h = int(input("Введите высоту полета: "))
v = int(input("Введите скорость тела: "))

E = E(m, h, v)
print(f"Полная механическая энергия: {E} Дж")
