

# 入力
N = int(input())
C = [0]
S = [0]
F = [0]
for i in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c-1)
    S.append(s-1)
    F.append(f-1)

# 出力
for i in range(1, N):
    t = 0
    for j in range(i, N):
        if t < S[j]:
            t = S[j]
        else:
            t = t + F[j] - (t % F[j])
        t += C[j]
    print(t)
