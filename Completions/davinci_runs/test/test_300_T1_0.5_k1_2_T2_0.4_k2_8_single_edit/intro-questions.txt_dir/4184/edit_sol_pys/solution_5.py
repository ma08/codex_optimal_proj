import sys
input = sys.stdin.readline



N = int(input())
W = list(map(int, input().split()))

min_diff = 100 * N
for i in range(1, N):
    s1 = sum(W[:i])
    s2 = sum(W[i:])
    min_diff = min(min_diff, abs(s1 - s2))

print(min_diff)
