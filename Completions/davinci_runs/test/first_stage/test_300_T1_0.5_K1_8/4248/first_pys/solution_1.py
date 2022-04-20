

import math

def calc_angle(x1, y1, x2, y2):
    # calculate the angle between the two points
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx)
    return angle

def calc_area(points):
    # calculate the area of the polygon
    # given a list of points
    area = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) / 2.0
    return area

def calc_tangent(points):
    # calculate the tangent to the polygon
    # given a list of points
    # the tangent is the line that is the longest
    # distance between two points
    tangent = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(1/2)
            if dist > tangent:
                tangent = dist
    return tangent

def calc_circumference(points):
    # calculate the circumference of the polygon
    # given a list of points
    # the circumference is the sum of the length of all sides
    circumference = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**(1/2)
        circumference += dist
    return circumference

def solve_problem(points):
    # solve the problem
    # given a list of points
    # the solution is the circumference of the polygon
    # divided by the tangent of the polygon
    tangent = calc_tangent(points)
    circumference = calc_circumference(points)
    return circumference / tangent

def main():
    # read the number of points
    num_points = int(input())

    # read the points
    points = []
    for i in range(num_points):
        x, y = map(float, input().split())
        points.append((x, y))

    # sort the points by angle
    angles = []
    for i in range(num_points):
        angles.append(calc_angle(points[0][0], points[0][1], points[i][0], points[i][1]))
    points = [x for _,x in sorted(zip(angles, points))]

    # solve the problem
    answer = solve_problem(points)

    # print the answer
    print("{:.3f}".format(answer))

if __name__ == "__main__":
    main()