import numpy as np

def multiply(array):

  op = 1
  for element in array:
    op *= element
  return op

array_size = int(input("Введите размер массива: "))
element = []
for i in range(array_size):
  element.append(int(input(f"Введите элемент {i+1}: ")))

array = np.array(element)

op = multiply(array)
print(f"Произведение элементов массива: {op}")
