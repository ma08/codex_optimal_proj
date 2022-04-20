
N, M = map(int, input().split())
L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

L_min = min(L)
R_max = max(R)
if R_max - L_min + 1 < 0:
    print(0)
else:
    print(R_max - L_min + 1)
