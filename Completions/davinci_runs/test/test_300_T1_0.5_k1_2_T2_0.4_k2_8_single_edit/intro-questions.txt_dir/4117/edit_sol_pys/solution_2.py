
from itertools import combinations

n = int(input())
l = sorted(list(map(int, input().split())))

count = 0
for i in combinations(l, 3):  # 3つずつ取り出す
    if i[0] + i[1] > i[2]:  # 三角形になるか判定
        count += 1

print(count)
