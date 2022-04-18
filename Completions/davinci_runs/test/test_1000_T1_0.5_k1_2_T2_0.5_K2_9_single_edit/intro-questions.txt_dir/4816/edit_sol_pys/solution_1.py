
import math

x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = min(abs(x - x1), abs(x - x2))
dy = min(abs(y - y1), abs(y - y2))

print(math.sqrt(dx * dx + dy * dy))
