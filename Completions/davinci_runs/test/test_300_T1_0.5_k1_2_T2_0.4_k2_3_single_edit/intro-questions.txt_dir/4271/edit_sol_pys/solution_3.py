

from sys import stdin

n = int(stdin.readline())
dishes = [int(a) - 1 for a in stdin.readline().split()]
base_points = [int(a) for a in stdin.readline().split()]
additional_points = [int(a) for a in stdin.readline().split()]

total_points = 0
for i in range(n):
    dish = dishes[i]
    total_points += base_points[dish]
    if i != 0 and dishes[i - 1] == dish - 1 and dish != 0:
        total_points += additional_points[dish]

print(total_points)
