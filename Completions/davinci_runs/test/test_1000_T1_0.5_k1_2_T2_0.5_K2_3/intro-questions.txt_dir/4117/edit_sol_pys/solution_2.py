
from itertools import combinations

n = int(input()) # 整数の個数
l = sorted(list(map(int, input().split()))) # 整数をソート

count = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
