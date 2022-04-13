

N = int(input())
W = list(map(int, input().split()))
s1 = 0
s2 = 0
min_diff = 100 * N
for t in range(1, N):
    s1 += W[t-1]
    s2 += W[t]
    diff = abs(s1 - s2)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
