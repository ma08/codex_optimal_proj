

from sys import stdin

n = int(stdin.readline())
dishes = [int(a) for a in stdin.readline().split()]
base_points = [int(a) for a in stdin.readline().split()]
additional_points = [int(a) for a in stdin.readline().split()]

# print(n, dishes, base_points, additional_points)

total_points = 0
for i in range(n):
    dish = dishes[i]
    total_points += base_points[dish - 1]
    if i != 0 and dishes[i - 1] == dish:
        total_points += additional_points[dish - 2]

print(total_points)
