
# 入力
N = int(input())
C = [0]
S = [0]
F = [0]
for i in range(N-1):
    C.append(int(input().split()[0]))
    S.append(int(input().split()[1]))
    F.append(int(input().split()[2]))

# 出力
for i in range(N):
    t = 0
    for j in range(i, N-1):
        if t < S[j]:
            t = S[j]
        else:
            t = t + F[j] - t % F[j]
        t += C[j]
    print(t)
