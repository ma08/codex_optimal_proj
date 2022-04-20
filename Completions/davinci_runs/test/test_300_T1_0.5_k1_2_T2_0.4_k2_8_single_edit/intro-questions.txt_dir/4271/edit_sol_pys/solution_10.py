



def get_input():
    return [int(a) for a in stdin.readline().split()]

from sys import stdin

n = int(stdin.readline())
dishes = [int(a) - 1 for a in stdin.readline().split()]
base_points = get_input()
additional_points = get_input()

# print(n, dishes, base_points, additional_points)

total_points = 0
for i in range(n):
    dish = dishes[i]
    total_points += base_points[dish]
    if i != 0 and dishes[i - 1] == dish - 1:
        total_points += additional_points[dish - 1]

print(total_points)
