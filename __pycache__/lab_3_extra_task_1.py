import numpy as np

stringe = int(input("количество строк: "))
columns = int(input("количество столбов: "))

array1 = np.zeros((stringe, columns))
array2 = np.zeros((stringe, columns))
array3 = np.zeros((stringe, columns))

print("элементы:")
for i in range(stringe):
    for j in range(columns):
        array1[i, j] = float(input(f"Введите элемент [{i}, {j}]: "))

print("элементы:")
for i in range(stringe):
    for j in range(columns):
        array2[i, j] = float(input(f"Введите элемент [{i}, {j}]: "))

for i in range(stringe):
    for j in range(columns):
        array3[i, j] = max(array1[i, j], array2[i, j])

print("Третий массив")
print(array3)
