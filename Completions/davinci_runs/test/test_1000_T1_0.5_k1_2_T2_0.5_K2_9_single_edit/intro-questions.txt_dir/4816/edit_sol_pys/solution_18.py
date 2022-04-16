x, y, x1, y1, x2, y2 = [int(x) for x in input().split()]
dist = 0


if x < x1:
    dist += x1 - x
elif x > x2:
    dist += x - x2

elif y < y1:
    dist += y1 - y
else:
    dist += y - y2

print(dist)
