

import itertools

n = int(input())
l = sorted(list(map(int, input().split())))

count = 0
for i in itertools.combinations(l, 3):
    if i[0] + i[1] > i[2]:
        count += 1

print(count)
