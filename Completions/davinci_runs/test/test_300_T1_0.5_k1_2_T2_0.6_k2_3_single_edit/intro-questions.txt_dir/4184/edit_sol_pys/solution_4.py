

import itertools

N = int(input())
t = tuple(map(int, input().split()))

ans = 0
for comb in itertools.combinations(t, 3):
    if comb[0] != comb[1] and comb[0] != comb[2] and comb[1] != comb[2]:
        ans += 1

print(ans)
