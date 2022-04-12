
from math import sin, cos, radians

N, g = map(float, input().split())  # N is the number of test cases and g is the gravity


def get_velocity(D, theta):  # D is the distance and theta is the angle
    g_theta = g * cos(radians(theta))
    return ((2 * D * g_theta) / g) ** 0.5

for i in range(int(N)):
    D, theta = map(float, input().split())
    print(get_velocity(D, theta))
