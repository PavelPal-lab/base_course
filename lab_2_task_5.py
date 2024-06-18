a = int(input('первое число'))
b = int(input('второе число'))
if b == 0:
    print('нельзя')
else:
    n = a // b
    x = a % b
    if x == 0:
        print(f'{a} делться на {b} без остатка.')
    else:
        print(f'{a} не делться на {b} нацело.')
    print(f'Целое: {n}')
    print(f'Остаток: {x}')


