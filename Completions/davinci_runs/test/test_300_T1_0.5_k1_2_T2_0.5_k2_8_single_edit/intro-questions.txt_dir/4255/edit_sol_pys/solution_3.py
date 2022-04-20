
import math

abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    print("Не существует такого треугольника")
