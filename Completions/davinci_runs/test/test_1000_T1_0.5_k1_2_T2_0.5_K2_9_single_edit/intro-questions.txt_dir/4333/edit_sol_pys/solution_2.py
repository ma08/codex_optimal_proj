

x1, y1, x2, y2 = map(int, input().split())  # input 4 number

if x1 == x2:
    y3 = y1
    y4 = y2
    x3 = x4 = x1 + (y2 - y1)
else:
    x3 = x1
    x4 = x2
    y3 = y4 = y1 + (x2 - x1)

print(x3, y3, x4, y4)
