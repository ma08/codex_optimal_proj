import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

MOD = 10 ** 9 + 7

# 前計算
F = [1] * (N + 1)
for i in range(1, N + 1):
    F[i] = F[i - 1] * i % MOD

# 階乗の逆元
INV = [1] * (N + 1)
INV[N] = pow(F[N], MOD - 2, MOD)
for i in range(N, 0, -1):
    INV[i - 1] = INV[i] * i % MOD


def cmb(n, r):
    if n < r:
        return 0
    r = min(r, n - r)
    return F[n] * INV[r] * INV[n - r] % MOD


ans = 0
for i in range(N):
    ans += (M - A[i]) * cmb(N - i - 1, 2)
    ans %= MOD

print(ans)
