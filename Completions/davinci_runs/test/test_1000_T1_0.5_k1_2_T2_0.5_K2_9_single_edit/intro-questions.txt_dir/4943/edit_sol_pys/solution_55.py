

from sys import stdin, stdout
from math import sqrt

n = int(stdin.readline())

points = []
for _ in range(n):
    points.append(tuple(map(float, stdin.readline().split())))

area = float(stdin.readline())

# calculate area of the original shape
orig_area = 0
for i in range(n):
    orig_area += points[i][0]*points[(i+1)%n][1] - points[i][1]*points[(i+1)%n][0]
orig_area = abs(orig_area) / 2

# calculate centroid of the original shape
centroid = (0, 0)
for i in range(n):
    centroid = (centroid[0] + (points[i][0] + points[(i+1)%n][0]) * (points[i][0]*points[(i+1)%n][1] - points[(i+1)%n][0]*points[i][1]),
                centroid[1] + (points[i][1] + points[(i+1)%n][1]) * (points[i][0]*points[(i+1)%n][1] - points[(i+1)%n][0]*points[i][1]))
centroid = (centroid[0] / (6 * orig_area), centroid[1] / (6 * orig_area))

# calculate distance from each point to the centroid
distances = []
for point in points:
    distances.append(sqrt((point[0] - centroid[0])**2 + (point[1] - centroid[1])**2))

# calculate the scaling factor
scale = sqrt(area / orig_area)

# scale the points
for i in range(len(points)):
    points[i] = (points[i][0] + scale * (points[i][0] - centroid[0]) - points[i][0],
                 points[i][1] + scale * (points[i][1] - centroid[1]) - points[i][1])

# move the points so that x, y >= 0 (min_x, min_y)
min_x = min(points, key=lambda p: p[0])[0]
min_y = min(points, key=lambda p: p[1])[1]
for i in range(len(points)):
    points[i] = (points[i][0] - min_x, points[i][1] - min_y)

# print the new points
for point in points:
    stdout.write('%.4f %.4f\n' % point)
