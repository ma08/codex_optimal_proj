n = int(input())
s = list(map(int, input().split()))


s.sort()

ans = 0.0
for i in range(1, n):
    ans += s[i] - s[i-1]

ans = 0
for i in range(1, n):
    if x[i] - x[i-1] > 1:
        ans += x[i] - x[i-1] - 1

print(ans)
