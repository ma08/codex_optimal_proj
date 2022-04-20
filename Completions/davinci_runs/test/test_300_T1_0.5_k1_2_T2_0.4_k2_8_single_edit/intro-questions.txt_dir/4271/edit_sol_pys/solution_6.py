

from sys import stdin

n = int(stdin.readline())
dishes = [int(a) - 1 for a in stdin.readline().split()]  # -1 to make it 0-indexed
base_points = [int(a) for a in stdin.readline().split()]
additional_points = [int(a) for a in stdin.readline().split()]

total_points = 0
for i in range(n):
    dish = dishes[i]  # dish = dish number
    total_points += base_points[dish]  # add base points
    if i != 0 and dishes[i - 1] == dish - 1:  # if not first dish and previous dish is one less
        total_points += additional_points[dish - 1]  # add additional points

print(total_points)
