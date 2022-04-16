
x, y, x1, y1, x2, y2 = [int(i) for i in input().split()]

if x1 <= x <= x2 and y1 <= y <= y2:
    x = min(abs(x1 - x), abs(x2 - x))
    y = min(abs(y1 - y), abs(y2 - y))
    print(min(x, y))

elif x1 <= x <= x2:
    print(min(abs(y1 - y), abs(y2 - y)))

elif y1 <= y <= y2:
    print(min(abs(x1 - x), abs(x2 - x)))

else:
    print(min(abs(x - x1) + abs(y - y1),
              abs(x - x2) + abs(y - y1),
              abs(x - x1) + abs(y - y2),
              abs(x - x2) + abs(y - y2)))
