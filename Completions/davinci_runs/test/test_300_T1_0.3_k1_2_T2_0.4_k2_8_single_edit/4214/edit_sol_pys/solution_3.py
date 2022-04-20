

import math
import itertools

def main():
    # 入力
    N = int(input())
    towns = [tuple(map(int, input().split())) for _ in range(N)]

# 各順列について、移動距離を計算
distances = []
for permutation in permutations:
    distance = 0
    for i in range(N-1):
        distance += math.sqrt((permutation[i][0] - permutation[i+1][0])**2 + (permutation[i][1] - permutation[i+1][1])**2)
    distances.append(distance)

# 平均を計算
print(sum(distances) / len(distances))
