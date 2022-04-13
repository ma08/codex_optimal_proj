# A
N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
dist = 0
for i in range(N):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break
print(cnt)

# B
N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        cnt += 1
print(cnt)

# C
N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0
for i in range(1, N):
    ans += A[i] - A[i - 1]
print(ans)

# D
N, K = map(int, input().split())


def cmb(n, r, mod=10**9+7):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


mod = 10**9+7  # 出力の制限
NN = 10**6
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, NN + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod//i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

ans = 0
for i in range(1, K + 1):
    ans += i * cmb(N - K + 1, i)
    ans %= mod
print(ans)
