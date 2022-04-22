
#input
import math

n, d = map(int, input().split()) #n is the number of points, d is the number of dimensions

points = []
for _ in range(n):
    points.append(list(map(int, input().split()))) #points is a list of lists, with each sublist containing the coordinates of a point

def distance(p1, p2):
    dist = 0
    for i in range(d):
        dist += (p1[i] - p2[i]) ** 2
    return math.sqrt(dist)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(points[i], points[j]).is_integer(): #if the distance between two points is an integer, add 1 to the count
            count += 1

print(count)
