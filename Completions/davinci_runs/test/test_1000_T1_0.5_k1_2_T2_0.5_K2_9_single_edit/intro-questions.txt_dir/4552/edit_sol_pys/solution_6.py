

N = int(input())
F = [[int(j) for j in input().split()] for _ in range(N)]
P = [int(k) for k in input().split()]

ans = -100000000
for i in range(1, 2**10):
    if bin(i).count('1') == 0:
        continue
    tmp = 0
    for j in range(N):
        cnt = 0
        for k in range(10):
            cnt += F[j][k] * ((i >> k) & 1)
        tmp += P[cnt]
    ans = max(ans, tmp)
print(ans)
