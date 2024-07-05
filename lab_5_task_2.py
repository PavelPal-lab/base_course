import numpy as np

name = input('ваше фамилия и имя: ')

name_upper = '_'.join(name.upper())
print('имя и фамилия в верх. регистре: ', name_upper)

ascii_codes_upper = np.array([ord(char) for char in name_upper])
print('ASCII верх. регистр: ', ascii_codes_upper)

name_lower = '_'.join(name.lower())
print('имя и фамилия в ниж. регистре: ', name_lower)

ascii_codes_lower = np.array([ord(char) for char in name_lower])
print('ASCII ниж. регистр: ', ascii_codes_lower)

max_value = np.max(np.concatenate([ascii_codes_upper, ascii_codes_lower]))
print('наибольшее значение: ', max_value)
min_value = np.min(np.concatenate([ascii_codes_upper, ascii_codes_lower]))
print('наименьшее значение: ', min_value)
