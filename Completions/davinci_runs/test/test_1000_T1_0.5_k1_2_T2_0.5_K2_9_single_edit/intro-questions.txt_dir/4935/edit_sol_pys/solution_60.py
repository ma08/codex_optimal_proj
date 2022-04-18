
"""
    File: file
    Author: Patrick J. Smith
    Date: 9/18/2016
    Description:
"""

from math import sin, cos, radians

N, g = map(float, input().split())


def get_velocity(d, theta):
    """
    Calculates the velocity of a projectile given the distance and angle.

    Args:
        d: the distance
        theta: the angle
    Returns:
        the velocity
    """
    g_theta = g * cos(radians(theta))
    return ((2 * d * g_theta) / g) ** 0.5


for i in range(int(N)):
    D, theta = map(int, input().split())
    print(get_velocity(D, theta))
