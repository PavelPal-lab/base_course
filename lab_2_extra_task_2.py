a = float(input("Введите длину отрезка a: "))
b = float(input("Введите длину отрезка b: "))
c = float(input("Введите длину отрезка c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник с такими сторонами не существует")
    