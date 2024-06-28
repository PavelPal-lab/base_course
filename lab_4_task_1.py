import numpy as np

first = int(input("первое число: "))
second = int(input("второе число: "))

lists = [first, second]
array = np.array(lists)

def average_value (array):
    av_va = (array[0] + array[1]) / 2
    return av_va

print(average_value(array))
