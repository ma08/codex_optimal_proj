

N, T = map(int, input().split())
d = {}
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if c not in d.keys():
            d[c] = t

print(min(d.keys()))
