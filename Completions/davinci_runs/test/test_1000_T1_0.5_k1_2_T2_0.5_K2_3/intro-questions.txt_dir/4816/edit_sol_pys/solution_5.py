import sys

x, y, x1, y1, x2, y2 = [int(i) for i in input().split()]

if x < x1:
    print(x1 - x, file=sys.stderr)
elif x > x2:
    print(x - x2, file=sys.stderr)
elif y < y1:
    print(y1 - y, file=sys.stderr)
else:
    print(y - y2, file=sys.stderr)
