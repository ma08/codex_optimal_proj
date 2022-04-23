
import itertools
import sys
import math

n = int(input())
coordinate = []
for i in range(n):
    coordinate.append(list(map(int, input().split())))

# 全組み合わせを作る
all_path = list(itertools.permutations(coordinate))
total_length = 0

for path in all_path:
    for i in range(n-1):
        total_length += math.sqrt(
            (path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i+1][1])**2)

print(total_length/len(all_path))
