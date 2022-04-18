
# this is a file
from itertools import combinations

n = int(input())
l = list(map(int, input().split()))

count = 0
for i in combinations(l, 2):
    if i[0] + i[1] > 0:
        count += 1

print(count)
