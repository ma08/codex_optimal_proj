
import sys
import math

# the number of vertices of the polygon
n = int(sys.stdin.readline())

# list of vertices of the polygon
vertices = []

# the area of the desired polygon
area = int(sys.stdin.readline())

# the current area of the polygon
current_area = 0.0

for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    vertices.append((x, y))
    if i != 0:
        current_area += x * vertices[i - 1][1] - y * vertices[i - 1][0]

# make the last point equal to the first point
vertices.append(vertices[0])

# the factor by which the polygon gets scaled
factor = math.sqrt(area / (current_area / 2))

# the new corners
new_vertices = []

for i in range(n):
    x = factor * vertices[i][0]
    y = factor * vertices[i][1]
    new_vertices.append((x, y))

# find the minimum x and y
min_x = sys.maxsize
min_y = sys.maxsize

for point in new_vertices:
    if point[0] < min_x:
        min_x = point[0]
    if point[1] < min_y:
        min_y = point[1]

# shift the polygon so that the minimum x and y is 0
for i in range(n):
    new_vertices[i] = (new_vertices[i][0] - min_x, new_vertices[i][1] - min_y)

# print the new corners
for point in new_vertices:
    print(point[0], point[1])
