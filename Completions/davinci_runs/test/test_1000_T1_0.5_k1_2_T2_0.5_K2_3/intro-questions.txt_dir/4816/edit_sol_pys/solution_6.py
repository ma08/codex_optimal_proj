

x1, y1, x2, y2 = [int(x) for x in input().split()]  # диапазон первой прямоугольной области
x3, y3 = [int(x) for x in input().split()]  # координаты проверяемой точки

if x3 < x1:
    print(x1 - x3)
elif x3 > x2:
    print(x3 - x2)
elif y3 < y1:
    print(y1 - y3)
else:
    print(y3 - y2)
