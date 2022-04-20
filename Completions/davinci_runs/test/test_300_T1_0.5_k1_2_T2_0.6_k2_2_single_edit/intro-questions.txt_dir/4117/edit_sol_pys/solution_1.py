
from itertools import combinations

n = int(input())
l = sorted(list(map(int, input().split())))  # sort the sides of the triangle

count = 0  # count the number of possible triangles
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
