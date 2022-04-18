import sys
import math

n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_closest(p, points):
    dists = [dist(p, point) for point in points]
    return points[dists.index(min(dists))]

def find_closest_points(p, points):
    dists = [dist(p, point) for point in points]
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min(dists)]

def find_closest_points_with_same_level(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) == max(points[i])]

def find_closest_points_with_higher_level(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) < max(points[i])]

def find_closest_points_with_lower_level(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) > max(points[i])]

def find_closest_points_with_higher_level_and_same_x(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) < max(points[i]) and p[0] == points[i][0]]

def find_closest_points_with_higher_level_and_same_y(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) < max(points[i]) and p[1] == points[i][1]]

def find_closest_points_with_higher_level_and_different_x(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) < max(points[i]) and p[0] != points[i][0]]

def find_closest_points_with_higher_level_and_different_y(p, points):
    dists = [dist(p, point) for point in points]
    min_dist = min(dists)
    return [points[i] for i in range(len(points)) 
        if dist(p, points[i]) == min_dist and max(p) < max(points[i]) and p[1] != points[i][1]]

def solve_easy(points):
    res = 0
    p = (0, 0)
    while len(points) > 0:
        p = find_closest(p, points)
        res += dist(p, (0, 0))
        points.remove(p)
    return res

def solve_hard(points):
    res = 0
    p = (0, 0)
    while len(points) > 0:
        closest_points = find_closest_points(p, points)
        if len(closest_points) == 1:
            p = closest_points[0]
            res += dist(p, (0, 0))
            points.remove(p)
        else:
            closest_points_with_same_level = find_closest_points_with_same_level(p, points)
            if len(closest_points_with_same_level) > 0:
                p = closest_points_with_same_level[0]
                res += dist(p, (0, 0))
                points.remove(p)
            else:
                closest_points_with_higher_level = find_closest_points_with_higher_level(p, points)
                if len(closest_points_with_higher_level) > 0:
                    p = closest_points_with_higher_level[0]
                    res += dist(p, (0, 0))
                    points.remove(p)
                else:
                    closest_points_with_lower_level = find_closest_points_with_lower_level(p, points)
                    if len(closest_points_with_lower_level) > 0:
                        p = closest_points_with_lower_level[0]
                        res += dist(p, (0, 0))
                        points.remove(p)
                    else:
                        closest_points_with_higher_level_and_same_x = find_closest_points_with_higher_level_and_same_x(p, points)
                        if len(closest_points_with_higher_level_and_same_x) > 0:
                            p = closest_points_with_higher_level_and_same_x[0]
                            res += dist(p, (0, 0))
                            points.remove(p)
                        else:
                            closest_points_with_higher_level_and_same_y = find_closest_points_with_higher_level_and_same_y(p, points)
                            if len(closest_points_with_higher_level_and_same_y) > 0:
                                p = closest_points_with_higher_level_and_same_y[0]
                                res += dist(p, (0, 0))
                                points.remove(p)
                            else:
                                closest_points_with_higher_level_and_different_x = find_closest_points_with_higher_level_and_different_x(p, points)
                                if len(closest_points_with_higher_level_and_different_x) > 0:
                                    p = closest_points_with_higher_level_and_different_x[0]
                                    res += dist(p, (0, 0))
                                    points.remove(p)
                                else:
                                    closest_points_with_higher_level_and_different_y = find_closest_points_with_higher_level_and_different_y(p, points)
                                    if len(closest_points_with_higher_level_and_different_y) > 0:
                                        p = closest_points_with_higher_level_and_different_y[0]
                                        res += dist(p, (0, 0))
                                        points.remove(p)
    return res

def solve(points):
    res = 0
    p = (0, 0)
    while len(points) > 0:
        closest_points = [point for point in points if dist(p, point) == min([dist(p, point) for point in points])]
        if len(closest_points) == 1:
            p = closest_points[0]
            res += dist(p, (0, 0))
            points.remove(p)
        else:
            closest_points_with_same_level = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) == max(point)]
            if len(closest_points_with_same_level) > 0:
                p = closest_points_with_same_level[0]
                res += dist(p, (0, 0))
                points.remove(p)
            else:
                closest_points_with_higher_level = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) < max(point)]
                if len(closest_points_with_higher_level) > 0:
                    p = closest_points_with_higher_level[0]
                    res += dist(p, (0, 0))
                    points.remove(p)
                else:
                    closest_points_with_lower_level = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) > max(point)]
                    if len(closest_points_with_lower_level) > 0:
                        p = closest_points_with_lower_level[0]
                        res += dist(p, (0, 0))
                        points.remove(p)
                    else:
                        closest_points_with_higher_level_and_same_x = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) < max(point) and p[0] == point[0]]
                        if len(closest_points_with_higher_level_and_same_x) > 0:
                            p = closest_points_with_higher_level_and_same_x[0]
                            res += dist(p, (0, 0))
                            points.remove(p)
                        else:
                            closest_points_with_higher_level_and_same_y = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) < max(point) and p[1] == point[1]]
                            if len(closest_points_with_higher_level_and_same_y) > 0:
                                p = closest_points_with_higher_level_and_same_y[0]
                                res += dist(p, (0, 0))
                                points.remove(p)
                            else:
                                closest_points_with_higher_level_and_different_x = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) < max(point) and p[0] != point[0]]
                                if len(closest_points_with_higher_level_and_different_x) > 0:
                                    p = closest_points_with_higher_level_and_different_x[0]
                                    res += dist(p, (0, 0))
                                    points.remove(p)
                                else:
                                    closest_points_with_higher_level_and_different_y = [point for point in points if dist(p, point) == min([dist(p, point) for point in points]) and max(p) < max(point) and p[1] != point[1]]
                                    if len(closest_points_with_higher_level_and_different_y) > 0:
                                        p = closest_points_with_higher_level_and_different_y[0]
                                        res += dist(p, (0, 0))
                                        points.remove(p)
    return res

print(solve(points))
