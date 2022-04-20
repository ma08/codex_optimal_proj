
import itertools
import sys
import numpy as np
import math

N = 5
coordinate = np.array([[1,1],[2,2],[3,3],[4,4],[5,5]])

# N = int(input())
# coordinate = []
# for i in range(N):
#     coordinate.append(list(map(int, input().split())))

# 全組み合わせを作る
all_path = list(itertools.permutations(coordinate, N))
total_length = 0

for path in all_path:
    for i in range(N-1):
        total_length += math.sqrt(
            (path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i+1][1])**2)

print(total_length/len(all_path))
