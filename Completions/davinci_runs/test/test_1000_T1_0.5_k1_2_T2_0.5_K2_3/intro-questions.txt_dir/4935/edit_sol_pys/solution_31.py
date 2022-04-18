

import sys
from math import sin, cos, radians

N, g = list(map(float, sys.stdin.readline().split()))

def get_velocity(D, theta):
    g_theta = g * cos(radians(theta))
    return ((2 * D * g_theta) / g) ** 0.5

for i in range(int(N)):
    D, theta = list(map(float, sys.stdin.readline().split()))
    print(get_velocity(D, theta))
