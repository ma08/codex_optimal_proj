
N = int(input())
W = [int(x) for x in input().split(' ')]

max_diff = float('inf')
for t in range(1, N):
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    if abs(s1 - s2) < max_diff:
        max_diff = abs(s1 - s2)

print(max_diff)
