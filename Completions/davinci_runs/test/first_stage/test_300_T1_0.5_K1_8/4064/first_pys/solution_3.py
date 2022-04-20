

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

d = [0] * h
for i in range(n):
    d[i % h] += 1

ans = 0
for i in range(l, r + 1):
    ans = max(ans, d[i])

print(ans)