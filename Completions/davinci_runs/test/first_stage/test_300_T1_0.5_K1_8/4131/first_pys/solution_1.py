

# ε₯ε
N, M = map(int, input().split())
P = []
Y = []
for _ in range(M):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)

# εΊε
for i in range(M):
    p = P[i]
    y = Y[i]
    print('{:0=6d}{:0=6d}'.format(p, Y.count(y)))