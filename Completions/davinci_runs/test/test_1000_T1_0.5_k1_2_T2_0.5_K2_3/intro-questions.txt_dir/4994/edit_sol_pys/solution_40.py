

x1, y1 = map(int, input().split()) # читаем из входного файла три пары чисел
x2, y2 = map(int, input().split()) # и преобразуем их в целые
x3, y3 = map(int, input().split()) # числа

if x1 == x2: # если первые две пары имеют одинаковые абсциссы, то
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print(x4, y4)
