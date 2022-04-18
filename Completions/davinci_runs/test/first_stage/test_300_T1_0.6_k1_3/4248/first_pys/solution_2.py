

import sys
from math import atan2, degrees

# This function is taken from https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
# Given three colinear points p, q, r, the function checks if
# point q lies on line segment 'pr'
def onSegment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are colinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    # See https://www.geeksforgeeks.org/orientation-3-ordered-points/
    # for details of below formula.
    val = (float(q[1]) - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if (val > 0):
        # Clockwise orientation
        return 1
    elif (val < 0):
        # Counterclockwise orientation
        return 2
    else:
        # Colinear orientation
        return 0

# The main function that returns true if line segment 'p1q1'
# and 'p2q2' intersect.
def doIntersect(p1, q1, p2, q2):
    # Find the four orientations needed for general and
    # special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2 and o3 != o4):
        return True

    # Special Cases
    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)):
        return True

    # p1, q1 and q2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)):
        return True

    # p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and onSegment(p2, p1, q2)):
        return True

     # p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and onSegment(p2, q1, q2)):
        return True

    # Doesn't fall in any of the above cases
    return False

def get_angle(p, q):
    x = q[0] - p[0]
    y = q[1] - p[1]
    return degrees(atan2(y, x))

def get_min_angle_diff(points):
    angles = []
    for i in range(len(points)):
        angles.append(get_angle(points[0], points[i]))
    angles.sort()
    min_diff = float('inf')
    for i in range(len(angles) - 1):
        diff = angles[i+1] - angles[i]
        if diff < min_diff:
            min_diff = diff
    diff = angles[0] - angles[-1] + 360
    if diff < min_diff:
        min_diff = diff
    return min_diff


def main():
    num_points = int(input())
    points = []
    for i in range(num_points):
        line = sys.stdin.readline()
        points.append(list(map(float, line.split())))

    min_angle_diff = float('inf')
    for i in range(num_points):
        for j in range(num_points):
            if i == j:
                continue
            p1 = points[i]
            p2 = points[j]
            q1 = [p1[0] + 1, p1[1]]
            q2 = [p2[0] + 1, p2[1]]
            intersects = False
            for k in range(num_points):
                if k == i or k == j:
                    continue
                for l in range(k+1, num_points):
                    if l == i or l == j:
                        continue
                    if doIntersect(p1, q1, points[k], points[l]):
                        intersects = True
                        break
                    if doIntersect(p2, q2, points[k], points[l]):
                        intersects = True
                        break
                if intersects:
                    break
            if not intersects:
                angle_diff = get_min_angle_diff(points)
                if angle_diff < min_angle_diff:
                    min_angle_diff = angle_diff
    print('{0:.3f}'.format(min_angle_diff))

if __name__ == '__main__':
    main()