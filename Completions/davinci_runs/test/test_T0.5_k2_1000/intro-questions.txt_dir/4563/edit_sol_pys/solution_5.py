from math import gcd
N = int(input())
A = []
for _ in range(N):
    T, X = map(int, input().split())
    A.append([T, X])

l = A[0][0]
r = A[0][1]
for i in range(1, N):
    l = l * A[i][0] // gcd(l, A[i][0])
    r = r * A[i][1] // gcd(r, A[i][1])

print(l+r)
