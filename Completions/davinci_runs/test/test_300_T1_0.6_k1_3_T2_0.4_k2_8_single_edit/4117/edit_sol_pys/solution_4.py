

from itertools import combinations

n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in combinations(l, 3):
    if i[0] + i[1] > i[2] and i[0] + i[2] > i[1] and i[1] + i[2] > i[0]:
        ans += 1
print(ans)
