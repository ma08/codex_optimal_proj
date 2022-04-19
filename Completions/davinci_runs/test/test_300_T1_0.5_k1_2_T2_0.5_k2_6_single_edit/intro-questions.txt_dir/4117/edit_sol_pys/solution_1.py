
from itertools import combinations

n = int(input())
l = list(map(int, input().split()))
l.sort()

count = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
