

import sys

def compute_angle(x, y):
    """
    This function computes the angle between the line formed by the origin and the
    point (x, y) and the x-axis.
    """
    if x == 0:
        if y > 0:
            return 90
        elif y < 0:
            return 270
        else:
            return 0
    elif y == 0:
        if x > 0:
            return 0
        else:
            return 180
    else:
        if x > 0 and y > 0:
            return math.degrees(math.atan(y / x))
        elif x < 0 and y > 0:
            return 180 + math.degrees(math.atan(y / x))
        elif x < 0 and y < 0:
            return 180 + math.degrees(math.atan(y / x))
        else:
            return 360 + math.degrees(math.atan(y / x))


def get_angle_difference(angle1, angle2):
    """
    This function computes the difference between two angles.
    """
    if angle1 > angle2:
        return angle1 - angle2
    else:
        return angle2 - angle1

# Get the number of points.
n = int(sys.stdin.readline())

# Get the points.
points = []
for i in range(n):
    point = sys.stdin.readline().split()
    points.append((float(point[0]), float(point[1])))

# Get the angles of the points.
angles = []
for i in range(n):
    angles.append(compute_angle(points[i][0], points[i][1]))

# Find the minimum angle difference.
min_angle_difference = 360
for i in range(n):
    for j in range(i + 1, n):
        angle_difference = get_angle_difference(angles[i], angles[j])
        if angle_difference < min_angle_difference:
            min_angle_difference = angle_difference

# Print the answer.
print(min_angle_difference)