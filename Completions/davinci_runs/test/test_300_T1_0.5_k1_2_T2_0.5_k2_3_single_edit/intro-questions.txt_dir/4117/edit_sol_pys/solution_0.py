

import numpy as np

from itertools import combinations

n = int(input())  # 入力
l = sorted(list(map(int, input().split())))  # 入力
# 三角形数を数える

count = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)  # 出力

# 入力
n, m = map(int, input().split())
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

# 出力
print(np.dot(a, b))
