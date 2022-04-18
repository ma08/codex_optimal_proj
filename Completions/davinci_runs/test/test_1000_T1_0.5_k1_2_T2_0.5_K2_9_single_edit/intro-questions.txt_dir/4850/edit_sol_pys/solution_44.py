
import math

n = int(input())

max_x, max_y = 0, 0

for i in range(n):
    a, b, c = map(int, input().split())
    x = a / 2
    y = math.sqrt(c ** 2 - x ** 2)
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y

print(round(max_x + max_y, 2))
