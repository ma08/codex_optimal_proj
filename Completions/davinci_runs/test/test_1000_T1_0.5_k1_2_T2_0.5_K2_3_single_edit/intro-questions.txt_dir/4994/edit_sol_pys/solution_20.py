

# Read input
x1, y1, x2, y2, x3, y3 = [int(i) for i in input().split()]

# Find the missing point
if x1 == x2:
    x = x3
else:
    x = x1

if y1 == y2:
    y = y3
else:
    y = y1

print(x, y)
