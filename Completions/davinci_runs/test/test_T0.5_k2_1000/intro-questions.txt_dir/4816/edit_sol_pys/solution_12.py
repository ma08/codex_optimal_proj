
x, y, x1, y1, x2, y2 = [int(i) for i in input().split()]

if x < x1 or x > x2:
    print(x1 - x)
elif y < y1 or y > y2:
    print(y1 - y)
else:
    print(y - y2)
