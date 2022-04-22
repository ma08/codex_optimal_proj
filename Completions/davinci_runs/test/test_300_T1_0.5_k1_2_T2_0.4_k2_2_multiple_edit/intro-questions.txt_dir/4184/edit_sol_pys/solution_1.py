N = int(input())
W = list(map(int, input().split()))

min_diff = 100 * N
for t in range(1, N):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    diff = abs(s1 - s2)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
