import sys
input = sys.stdin.readline


N = int(input()) - 1
A = list(map(int, input().split())) + [1]

ans = 0

for i in range(N):
    ans += A[i] * A[i + 1]

print(count % (10 ** 9 + 7))
