
x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()

if x1 == x2:
    x4 = int(x3)
elif x1 == x3:
    x4 = int(x2)
else:
    x4 = int(x1)

if y1 == y2:
    y4 = int(y3)
elif y1 == y3:
    y4 = int(y2)
else:
    y4 = int(y1)

print(x4, y4)
