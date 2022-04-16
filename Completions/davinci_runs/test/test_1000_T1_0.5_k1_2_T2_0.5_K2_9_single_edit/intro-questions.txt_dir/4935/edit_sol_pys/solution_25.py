
from math import sin, cos, radians

N, g = map(float, input().split())  # number of test cases and acceleration due to gravity


def get_velocity(D, theta):  # function to calculate the velocity
    g_theta = g * cos(radians(theta))
    return ((2 * D * g_theta) / g) ** 0.5

for i in range(int(N)):
    D, theta = map(int, input().split())
    print(get_velocity(D, theta))
