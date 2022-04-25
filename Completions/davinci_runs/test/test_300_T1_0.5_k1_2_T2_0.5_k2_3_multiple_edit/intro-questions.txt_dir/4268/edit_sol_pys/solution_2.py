
# take input from user
import math

n, d = map(int, input().split())
# define points list


# append points in list
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))
# define method to calculate distance

def distance(p1, p2):
    dist = 0
    for i in range(d):
        dist += (p1[i] - p2[i]) ** 2
    return math.sqrt(dist)
# define count variable

count = 0

# check if distance is integer or not
for i in range(n):
    for j in range(i + 1, n):
        if distance(points[i], points[j]).is_integer():
            count += 1

# print count
print(count)
