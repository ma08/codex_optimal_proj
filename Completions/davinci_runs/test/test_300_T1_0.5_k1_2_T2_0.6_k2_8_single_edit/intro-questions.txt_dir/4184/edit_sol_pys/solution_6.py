
N = int(input())
W = list(map(int, input().split()))

min_diff = 100 * N
for t in range(1, N):  # t: 前半分の終わり
    s1 = sum(W[:t])
    s2 = sum(W[t:])
    diff = abs(s1 - s2)
    min_diff = min(diff, min_diff)

print(min_diff)
