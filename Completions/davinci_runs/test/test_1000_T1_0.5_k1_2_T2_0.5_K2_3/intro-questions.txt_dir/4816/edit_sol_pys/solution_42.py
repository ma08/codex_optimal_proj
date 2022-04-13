

x, y, x1, y1, x2, y2 = [int(i) for i in input().strip().split()]

if x < x1:
    print(x1 - x)
elif x > x2:
    print(x - x2)
elif y < y1:
    print(y1 - y)
else:
    print(y - y2)
