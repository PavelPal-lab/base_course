n = int(input('Число'))
if n <= 0:
    print(n)
else:
    a = 1
    b = 1
    print(a)
    for i in range(n - 1):
        print(b)
        a, b = b, a + b 
