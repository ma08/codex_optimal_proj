
# read the input
from sys import stderr
from sys import stdin

n = int(input())
dishes = [int(a) - 1 for a in input().split()]
base_points = [int(a) for a in input().split()]
additional_points = [int(a) for a in input().split()]

# calculate the total points
total_points = 0
for i in range(n):
    dish = dishes[i]
    total_points += base_points[dish]
    if i != 0 and dishes[i - 1] == dish - 1:
        total_points += additional_points[dish - 1]

print(total_points)

# print(n, file=stderr)
# print(dishes, file=stderr)
# print(base_points, file=stderr)
# print(additional_points, file=stderr)
