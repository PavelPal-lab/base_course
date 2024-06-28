import numpy as np

def S_figure(figure):

  if figure == "круг":
    r = int(input("радиус круга: "))
    S = np.pi * r**2
  elif figure == "прямоугольник":
    side1 = int(input("первая сторона: "))
    side2 = int(input("вторая сторона: "))
    S = side1 * side2
  elif figure == "треугольник":
    base = int(input("длина основания: "))
    h = int(input("высота треугольника: "))
    S = (base * h) / 2
  else:
    S = None
    print("фигня")
  return S

figure = input("тип фигуры (круг, прямоугольник, треугольник): ")

S = S_figure(figure)
if S is not None:
  print(f"Площадь {figure}а: {S}")
