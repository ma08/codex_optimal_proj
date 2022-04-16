
from math import sin, cos, radians

N, g = map(float, input().split()) # N = number of test cases, g = acceleration due to gravity

def get_velocity(D, theta): # D = distance, theta = angle
    g_theta = g * cos(radians(theta))
    return ((2 * D * g_theta) / g) ** 0.5 # v = sqrt(2D * g * cos(theta) / g)

for i in range(int(N)):
    D, theta = map(int, input().split())
    print(get_velocity(D, theta))
