import math

h, v = [int(i) for i in input().split()]
h = int(h)
v = int(v)
v = v*math.pi/180
print(math.ceil(h/math.sin(v)))
