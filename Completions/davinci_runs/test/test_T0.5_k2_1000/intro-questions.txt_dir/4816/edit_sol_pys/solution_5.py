
x, y, x1, y1, x2, y2 = [int(z) for z in input().split()]

print(max(0, x1 - x, x - x2, y1 - y, y - y2))
