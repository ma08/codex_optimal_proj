N, M = map(int, input().split())
L = []
R = []


for i in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

L_max = max(L)
R_min = min(R)
print(R_min - L_max + 1)
