import sys

# 入力
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# 解法
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        ans += 1
print(ans)
