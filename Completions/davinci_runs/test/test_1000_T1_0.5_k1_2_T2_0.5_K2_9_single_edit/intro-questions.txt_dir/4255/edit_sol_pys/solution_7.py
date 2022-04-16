
import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    print("Треугольник не существует")
