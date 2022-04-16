
x, y, x1, y1, x2, y2 = map(int, input().split())
print(min(abs(x - x1) + abs(y - y1), abs(x - x2) + abs(y - y1), abs(x - x1) + abs(y - y2), abs(x - x2) + abs(y - y2)))
