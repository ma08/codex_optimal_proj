
from collections import Counter
from sys import stdin

n = int(stdin.readline())
dishes = Counter([int(a) - 1 for a in stdin.readline().split()])
base_points = [int(a) for a in stdin.readline().split()] + [0]
additional_points = [int(a) for a in stdin.readline().split()] + [0]

total_points = 0
for i in range(n + 1):
    total_points += dishes[i] * base_points[i]
    if dishes[i - 1] > 0:
        total_points += dishes[i] * additional_points[i - 1]

print(total_points)
