

from math import sin, cos, radians

number_of_inputs, gravity = map(float, input().split())

def get_velocity(distance, theta):
    g_theta = gravity * cos(radians(theta))
    return ((2 * distance * g_theta) / gravity) ** 0.5

for i in range(int(number_of_inputs)):
    distance, theta = map(float, input().split())
    print(get_velocity(distance, theta))
