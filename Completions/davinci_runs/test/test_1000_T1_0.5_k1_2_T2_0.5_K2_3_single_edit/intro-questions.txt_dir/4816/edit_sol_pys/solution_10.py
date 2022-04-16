

x, y, x1, y1, x2, y2 = map(int, input().split())

if x1 <= x <= x2 and y1 <= y <= y2:
    x = min(x - x1, x2 - x)
    y = min(y - y1, y2 - y)
    print(min(x, y))

elif x1 <= x <= x2:
    print(min(y - y1, y2 - y))

elif y1 <= y <= y2:
    print(min(x - x1, x2 - x))

else:
    print(min((x - x1) + (y - y1), (x - x2) + (y - y1), (x - x1) + (y - y2), (x - x2) + (y - y2)))
