
x1, y1, x2, y2 = map(int, input().split())  # ввод координат первой и второй точек

if x1 == x2:  # если координаты первой точки равны координатам второй точки
    x3 = x1 + abs(y1 - y2)  # координата x третьей точки равна координате x первой точки + разница между координатами y первой и второй точки
    x4 = x1 - abs(y1 - y2)  # координата x четвертой точки равна координате x первой точки - разница между координатами y первой и второй точки
    y3 = y1  # координата y третьей точки равна координате y первой точки
    y4 = y2  # координата y четвертой точки равна координате y второй точки
elif y1 == y2:  # если координаты первой точки равны координатам второй точки
    x3 = x1  # координата x третьей точки равна координате x первой точки
    x4 = x2  # координата x четвертой точки равна координате x второй точки
    y3 = y1 + abs(x1 - x2)  # координата y третьей точки равна координате y первой точки + разница между координатами x первой и второй точки
    y4 = y1 - abs(x1 - x2)  # координата y четвертой точки равна координате y первой точки - разница между координатами x первой и второй точки
else:
    x3 = x2  # координата x третьей точки равна координате x второй точки
    y3 = y1  # координата y третьей точки равна координате y первой точки
    x4 = x1  # координата x четвертой точки равна координате x первой точки
    y4 = y2  # координата y четвертой точки равна координате y второй точки

print(x3, y3, x4, y4)  # вывод координат третьей и четвертой точек
