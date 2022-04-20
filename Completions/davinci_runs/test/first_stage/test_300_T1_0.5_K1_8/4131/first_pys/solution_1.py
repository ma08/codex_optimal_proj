

# 入力
N, M = map(int, input().split())
P = []
Y = []
for _ in range(M):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)

# 出力
for i in range(M):
    p = P[i]
    y = Y[i]
    print('{:0=6d}{:0=6d}'.format(p, Y.count(y)))