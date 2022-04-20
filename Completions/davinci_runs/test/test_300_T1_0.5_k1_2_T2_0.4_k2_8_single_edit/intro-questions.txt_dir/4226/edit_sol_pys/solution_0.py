import math


x, y = map(float, input().split())

if y % 2 == 0 and x * 2 <= y and y <= x * 4 and x >= 1:
    print('Yes')
else:
    print('No')
