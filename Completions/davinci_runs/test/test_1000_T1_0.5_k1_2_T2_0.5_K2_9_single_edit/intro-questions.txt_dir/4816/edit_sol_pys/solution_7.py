
x, y, x1, y1, x2, y2 = [int(x) for x in input().split()] # список из шести элементов

if x < x1:
    print(x1 - x) # координата х меньше левого края прямоугольника
elif x > x2:
    print(x - x2) # координата х больше правого края прямоугольника
elif y < y1:
    print(y1 - y)
else:
    print(y - y2)
