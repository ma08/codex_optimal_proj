

from sys import stdin

n = int(stdin.readline())
dishes = [int(a) - 1 for a in stdin.readline().split()]
base_points = [int(a) for a in stdin.readline().split()]
additional_points = [int(a) for a in stdin.readline().split()]

total_points = 0
for i in range(n):
    dish_index = dishes[i]
    total_points += base_points[dish_index]
    if i != 0 and dishes[i - 1] == dish_index:
        total_points += additional_points[dish_index]

print(total_points)
