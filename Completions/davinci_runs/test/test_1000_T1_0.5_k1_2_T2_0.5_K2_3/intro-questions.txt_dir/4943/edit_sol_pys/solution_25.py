
import sys
import math


n = int(input())


corners = []


area = int(input())


current_area = 0

for i in range(n):
    x, y = map(float, input().split())
    corners.append((x, y))
    if i != 0:
        current_area += x * corners[i - 1][1] - y * corners[i - 1][0]


corners.append(corners[0])


factor = math.sqrt(area / abs(current_area))

# the new corners
new_corners = []

for i in range(n):
    x = factor * corners[i][0]
    y = factor * corners[i][1]
    new_corners.append((x, y))

# find the minimum x and y
min_x = sys.maxsize
min_y = sys.maxsize

for point in new_corners:
    if point[0] < min_x:
        min_x = point[0]
    if point[1] < min_y:
        min_y = point[1]

# shift the polygon so that the minimum x and y are 0
for i in range(n):
    new_corners[i] = (new_corners[i][0] - min_x, new_corners[i][1] - min_y)

# print the new corners
for point in new_corners:
    print(point[0], point[1])
