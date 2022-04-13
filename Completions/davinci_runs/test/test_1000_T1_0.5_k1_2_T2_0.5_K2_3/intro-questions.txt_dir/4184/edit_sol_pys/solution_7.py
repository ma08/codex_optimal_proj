

N = int(input())
W = list(map(int, input().split()))
min_diff = sum(W)
for t in range(1, N - 1):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    min_diff = min(min_diff, abs(s1 - s2))

print(min_diff)
