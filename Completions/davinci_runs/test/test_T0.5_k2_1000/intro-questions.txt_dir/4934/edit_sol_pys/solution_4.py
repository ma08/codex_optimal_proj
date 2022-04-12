import math

h = int(input())
v = int(input())

v = v*math.pi/180

print(math.ceil(h/math.sin(v)))
