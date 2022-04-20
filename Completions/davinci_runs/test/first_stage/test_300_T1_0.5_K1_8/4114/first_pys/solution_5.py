

import sys

#Read lines from standard input
lines = [line.strip() for line in sys.stdin]

#Parse input
N = int(lines[0])
points = [(int(line.split(' ')[0]), int(line.split(' ')[1]), int(line.split(' ')[2])) for line in lines[1:]]

#Find lowest point and get its coordinates
min_point = min(points, key=lambda p: p[2])

#Find center coordinates by averaging x and y coordinates of all points
center_x = sum(point[0] for point in points) / len(points)
center_y = sum(point[1] for point in points) / len(points)

#Find height by adding the altitude of all points to the altitude of the lowest point
height = sum(point[2] for point in points) / len(points) + min_point[2]

#Print center coordinates and height
print(center_x, center_y, height)