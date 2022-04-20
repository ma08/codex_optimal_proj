

import math

def get_theta(points):
    # Get the point with the highest x-coordinate
    x_max = 0
    for point in points:
        if point[0] > x_max:
            x_max = point[0]
            x_max_point = point
    
    # Get the point with the highest y-coordinate
    y_max = 0
    for point in points:
        if point[1] > y_max:
            y_max = point[1]
            y_max_point = point
    
    # Get the point with the lowest x-coordinate
    x_min = 0
    for point in points:
        if point[0] < x_min:
            x_min = point[0]
            x_min_point = point
    
    # Get the point with the lowest y-coordinate
    y_min = 0
    for point in points:
        if point[1] < y_min:
            y_min = point[1]
            y_min_point = point
    
    # Get the point with the highest y-coordinate that is not the y_max_point
    y_max_2 = 0
    for point in points:
        if point[1] > y_max_2 and point != y_max_point:
            y_max_2 = point[1]
            y_max_2_point = point
    
    # Get the point with the lowest y-coordinate that is not the y_min_point
    y_min_2 = 0
    for point in points:
        if point[1] < y_min_2 and point != y_min_point:
            y_min_2 = point[1]
            y_min_2_point = point
    
    # Get the point with the highest x-coordinate that is not the x_max_point
    x_max_2 = 0
    for point in points:
        if point[0] > x_max_2 and point != x_max_point:
            x_max_2 = point[0]
            x_max_2_point = point
    
    # Get the point with the lowest x-coordinate that is not the x_min_point
    x_min_2 = 0
    for point in points:
        if point[0] < x_min_2 and point != x_min_point:
            x_min_2 = point[0]
            x_min_2_point = point
    
    # Get theta
    theta = 0
    if x_max_point[1] == y_max_point[1]:
        theta = math.pi / 2
    elif x_min_point[1] == y_min_point[1]:
        theta = math.pi / 2
    elif x_max_point[1] == y_min_point[1]:
        theta = 3 * math.pi / 2
    elif x_min_point[1] == y_max_point[1]:
        theta = 3 * math.pi / 2
    elif x_max_point[0] == y_max_point[0]:
        theta = 0
    elif x_min_point[0] == y_min_point[0]:
        theta = 0
    elif x_max_point[0] == y_min_point[0]:
        theta = math.pi
    elif x_min_point[0] == y_max_point[0]:
        theta = math.pi
    elif x_max_point[1] == y_max_2_point[1] and x_max_point[0] == x_max_2_point[0]:
        theta = math.atan((x_max_point[1] - x_max_2_point[1]) / (x_max_point[0] - x_max_2_point[0]))
    elif x_min_point[1] == y_min_2_point[1] and x_min_point[0] == x_min_2_point[0]:
        theta = math.atan((x_min_point[1] - x_min_2_point[1]) / (x_min_point[0] - x_min_2_point[0]))
    elif x_max_point[1] == y_min_2_point[1] and x_max_point[0] == x_min_2_point[0]:
        theta = math.atan((x_max_point[1] - x_min_2_point[1]) / (x_max_point[0] - x_min_2_point[0]))
    elif x_min_point[1] == y_max_2_point[1] and x_min_point[0] == x_max_2_point[0]:
        theta = math.atan((x_min_point[1] - x_max_2_point[1]) / (x_min_point[0] - x_max_2_point[0]))
    elif x_max_point[1] == y_min_2_point[1] and x_max_point[0] == x_min_2_point[0]:
        theta = math.atan((x_max_point[1] - x_min_2_point[1]) / (x_max_point[0] - x_min_2_point[0]))
    elif x_min_point[1] == y_max_2_point[1] and x_min_point[0] == x_max_2_point[0]:
        theta = math.atan((x_min_point[1] - x_max_2_point[1]) / (x_min_point[0] - x_max_2_point[0]))
    elif x_max_point[1] == y_max_2_point[1] and x_max_point[0] == x_max_2_point[0]:
        theta = math.atan((x_max_point[1] - x_max_2_point[1]) / (x_max_point[0] - x_max_2_point[0]))
    elif x_min_point[1] == y_min_2_point[1] and x_min_point[0] == x_min_2_point[0]:
        theta = math.atan((x_min_point[1] - x_min_2_point[1]) / (x_min_point[0] - x_min_2_point[0]))
    
    return theta

# Get input
n = int(input())
points = []
for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

# Get theta
theta = get_theta(points)

# Print theta
print(theta)