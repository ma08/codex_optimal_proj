
N = int(input())
A = []
for _ in range(N):
    T, X = map(int, input().split())
    A.append([T, X])

l = A[0][0]
r = A[0][1]
for i in range(1, N):
    l = lcm(l, A[i][0]) % MOD
    r = lcm(r, A[i][1]) % MOD

print(l+r)
