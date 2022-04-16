
from math import sin, cos, radians


def get_velocity(g, D, theta):
    g_theta = g * cos(radians(theta))
    return ((2 * D * g_theta) / g) ** 0.5


if __name__ == '__main__':
    N, g = map(float, input().split())
    for i in range(int(N)):
        D, theta = map(int, input().split())
        print(get_velocity(g, D, theta))
