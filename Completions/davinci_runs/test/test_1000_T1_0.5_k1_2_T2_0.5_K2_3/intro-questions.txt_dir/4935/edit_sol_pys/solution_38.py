
from math import sin, cos, radians

N, g = map(float, input().split()) # N is no. of test cases, g is acceleration due to gravity
# function to calculate velocity

def get_velocity(D, theta):
    g_theta = g * cos(radians(theta))
    return ((2 * D * g_theta) / g) ** 0.5

for i in range(int(N)):
    D, theta = map(float, input().split())
    print(get_velocity(D, theta))
