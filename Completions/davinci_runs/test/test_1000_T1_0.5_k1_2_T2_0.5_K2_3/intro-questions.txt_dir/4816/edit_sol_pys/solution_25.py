

x1, y1, x2, y2 = [int(x) for x in input().split()]  # считываем прямоугольник
x3, y3 = [int(x) for x in input().split()]  # считываем точку


if x3 < x1:  # если точка левее прямоугольника
    print(x1 - x3)
elif x3 > x2:  # если точка правее прямоугольника
    print(x3 - x2)
elif y3 < y1:  # если точка выше прямоугольника
    print(y1 - y3)
else:  # если точка ниже прямоугольника
    print(y3 - y2)
