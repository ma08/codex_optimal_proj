
# input
N = int(input())
C = []
S = []
F = []
for i in range(N-1):
    c, s, f = map(int, input().split()) # c:コスト, s:出発時刻, f:待ち時間
    C.append(c)
    S.append(s)
    F.append(f)

# output
for i in range(N):
    t = 0
    for j in range(i, N-1): # j:出発地
        if t < S[j]:
            t = S[j]
        else:
            t = t + F[j] - t % F[j]
        t += C[j]
    print(t)
