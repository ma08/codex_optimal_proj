

n = int(input())
w = list(map(int, input().split()))

min_diff = 100 * n
for t in range(1, n):
    s1 = sum(w[:t])
    s2 = sum(w[t:])
    diff = abs(s1 - s2)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
