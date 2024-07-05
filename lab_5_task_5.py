fio = input('введите фио латиницей: ')

upper_fio = [symbol.upper() for symbol in fio]
print(f'верхний регистр {upper_fio}')

lower_fio = [symbol.lower() for symbol in fio]
print(f'нижний регистр {lower_fio}')

sum_upper = sum(ord(symbol) for symbol in upper_fio)
print(f'сумма врехних регистров ASCII {sum_upper}')

sum_lower = sum(ord(symbol) for symbol in lower_fio)
print(f'сумма нижних регистров ASCII {sum_lower}')
