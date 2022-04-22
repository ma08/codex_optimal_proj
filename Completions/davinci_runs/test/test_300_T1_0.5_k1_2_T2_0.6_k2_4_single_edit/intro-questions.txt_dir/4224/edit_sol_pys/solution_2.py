# https://atcoder.jp/contests/abc169/tasks/abc169_b


import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# solve
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        ans += 1

print(ans)
