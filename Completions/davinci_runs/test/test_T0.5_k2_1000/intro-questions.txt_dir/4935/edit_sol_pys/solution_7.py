from math import sin, cos, radians

N, g = map(float, input().split())  # read N and g


def get_velocity(D, theta):  # get velocity
    g_theta = g * cos(radians(theta))  # get g * cos(theta)
    return ((2 * D * g_theta) / g) ** 0.5  # return velocity


for i in range(int(N)):  # loop N times
    D, theta = map(int, input().split())  # read D and theta
    print(get_velocity(D, theta))  # print velocity
