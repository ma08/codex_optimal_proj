

N, K = map(int, input().split())
S = input()

ans = ""
for i in range(N):
    if i < (K - 1) % N:
        ans += S[i]
    else:
        ans += S[(K - 1) % N]

print(ans)
