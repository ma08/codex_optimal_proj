

N, M = map(int, input().split())
L, R = [], []
for i in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

max_l = max(L)
min_r = min(R)

if min_r < max_l:
    print(0)
else:
    print(min_r - max_l + 1)