import math

r = int(input())  # The radius of the larger circle

area_of_circle_of_radius_1 = math.pi * 1 * 1
area_of_circle_of_radius_r = math.pi * r * r

print(int(area_of_circle_of_radius_r / area_of_circle_of_radius_1))
