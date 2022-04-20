#
# A - Power Socket
#
# https://atcoder.jp/contests/abc077/tasks/abc077_a
#


# input
N, M = map(int, input().split())

# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        ans += 1

print(ans)
