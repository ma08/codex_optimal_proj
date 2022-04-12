
#input
import math

h, v = [float(i) for i in input().split()]

v = v*math.pi/180

print(math.ceil(h/math.sin(v)))
