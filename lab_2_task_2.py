a = int(input('первый член'))
b = int(input('знаменатель'))
c = int(input('количество'))
for i in range(0, c, 1):
    n = a * (b ** i)
    print(n)