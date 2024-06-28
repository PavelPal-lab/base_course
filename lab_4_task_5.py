import numpy as np

def S_figure(figure):

  if figure == "круг":
    r = float(input("радиус круга: "))
    S = np.pi * r**2
  elif figure == "прямоугольник":
    side1 = float(input("первая сторона: "))
    side2 = float(input("вторая сторона: "))
    S = side1 * side2
  elif figure == "треугольник":
    base = float(input("длина основания: "))
    h = float(input("высота треугольника: "))
    S = (base * h) / 2
  else:
    S = None
    print("фигня")
  return S

figure = input("тип фигуры (круг, прямоугольник, треугольник): ")

S = S_figure(figure)
if S is not None:
  print(f"Площадь {figure}а: {S}")
