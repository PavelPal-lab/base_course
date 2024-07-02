#listcom 
symbols = 'Python'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes)

#genexp
symbols = 'Snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes)
for object in symbol_codes:
    print(object)

#map
def is_device_by_three(a):
    return(a%3 == 0)

nums = [24, 65, 23, -32, 75]
result = list(map(is_device_by_three, nums))

print(result)

def my_func(a, b):
    return a*b

nums1 = [6, 7, 8, 9, 10]
nums2 = [1, 2, 3, 4, 5]

nums_multiply = list(map(my_func, nums1,nums2))

print(nums_multiply)

#zip
names = ['John', 'David', 'Maria']
ages = [16, 25, 19, 41]
isTeenager = [True, False, True]

users = list(zip(names, ages, isTeenager))
print(users)

print('User age:', dict(zip(names, ages)))

#filter
names = ['John', 'David', 'Maria']
ages = [16, 25, 19, 41]

def checker(user):
    name, age = user
    return age > 21

users = list(zip(names, ages))
canDrinkAlcohol = list(filter(checker, users))
print(canDrinkAlcohol)

#sys and os
import sys, os

print(os.getcwd())

#os.system('echo hi!')
#os.system('python3 /workspaces/base_course/lec_5_dop_func.py')

print('Python version is:', sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))
print(dir(os))
print(dir(print))

#time
import time

timer = time.time()
for i in range(10):
    print(i)
    time.sleep(1)

print(f'{time.time() - timer}, seconds')