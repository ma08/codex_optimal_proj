from math import sin, radians, ceil

h, v = map(int, input().split())

print(math.ceil(h / math.sin(math.radians(v))))
