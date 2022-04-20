
from itertools import combinations

N = int(input())  # 入力
L = list(map(int, input().split()))  # 入力

comb = combinations(L, 3)

count = 0
for c in list(comb):
    if c[0] + c[1] > c[2] and c[1] + c[2] > c[0] and c[2] + c[0] > c[1]:
        count += 1

print(count)
