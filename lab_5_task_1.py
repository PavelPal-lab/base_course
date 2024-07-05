import numpy as np

N = int(input('длина массива: '))

array1 = np.random.randint(0, 100, size=N)
array2 = np.random.randint(0, 100, size=N)
array3 = np.random.randint(0, 100, size=N)

print('Массив 1: ', array1)
print('Массив 2: ', array2)
print('Массив 3: ', array3)

max_element = np.max([np.max(array1), np.max(array2), np.max(array3)])
print('наибольший элемент: ', max_element)

sum_elements = np.sum(array1) + np.sum(array2) + np.sum(array3)
print('сумма всех элементов: ', sum_elements)
