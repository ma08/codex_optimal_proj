

import math

def is_inside(a,b,c):
    """
    Determines if point c is inside triangle defined by points a,b
    """
    # Compute vectors
    v0 = [c[0] - a[0], c[1] - a[1]]
    v1 = [b[0] - a[0], b[1] - a[1]]
    v2 = [c[0] - b[0], c[1] - b[1]]
    # Compute dot products
    dot00 = v0[0] * v0[0] + v0[1] * v0[1]
    dot01 = v0[0] * v1[0] + v0[1] * v1[1]
    dot02 = v0[0] * v2[0] + v0[1] * v2[1]
    dot11 = v1[0] * v1[0] + v1[1] * v1[1]
    dot12 = v1[0] * v2[0] + v1[1] * v2[1]
    # Compute barycentric coordinates
    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom
    # Check if point is in triangle
    return (u >= 0) and (v >= 0) and (u + v < 1)

def find_angle(a,b):
    """
    Finds the angle between two vectors a and b
    """
    dot = a[0] * b[0] + a[1] * b[1]
    det = a[0] * b[1] - a[1] * b[0]
    return math.atan2(det, dot)

def find_area(a,b,c):
    """
    Finds the area of a triangle defined by points a,b,c
    """
    return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2

def find_triangle_area(a,b,c):
    """
    Finds the area of a triangle defined by points a,b,c
    """
    ab = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    ac = math.sqrt((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2)
    bc = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
    s = (ab + ac + bc) / 2
    return math.sqrt(s * (s - ab) * (s - ac) * (s - bc))

def main():
    n = int(input())
    points = []
    for i in range(n):
        x,y = [float(x) for x in input().split()]
        points.append([x,y])
    max_area = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                # Check if points are collinear
                if find_area(points[i],points[j],points[k]) < 1e-10:
                    continue
                # Check if points are inside triangle
                for l in range(n):
                    if l == i or l == j or l == k:
                        continue
                    if is_inside(points[i],points[j],points[l]) or is_inside(points[i],points[k],points[l]) or is_inside(points[j],points[k],points[l]):
                        break
                else:
                    # Find area of triangle
                    area = find_triangle_area(points[i],points[j],points[k])
                    if area > max_area:
                        max_area = area
    # Find angle
    angle = find_angle([1,0],[1,1]) + find_angle([1,1],[0,1]) + find_angle([0,1],[-1,0]) + find_angle([-1,0],[-1,-1]) + find_angle([-1,-1],[0,-1]) + find_angle([0,-1],[1,0])
    # Find radius
    r = math.sqrt(max_area / angle)
    print(2 * math.pi * r)

if __name__ == '__main__':
    main()