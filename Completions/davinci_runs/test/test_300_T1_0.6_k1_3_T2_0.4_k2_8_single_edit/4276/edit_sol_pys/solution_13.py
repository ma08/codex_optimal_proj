

N, T = map(int, input().split())
d = {}
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if c in d.keys():
            d[c] = min(d[c], t)
        else:
            d[c] = t
if len(d) == 0:
    print("TLE")
else:
    d = sorted(d.items(), key=lambda x: x[0])
    print(d[0][0])
