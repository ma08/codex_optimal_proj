n = int(input())
a = list(map(int, input().split()))

ans = 0
l = 0
r = 0
while l < n:
    while r < n and a[r] <= 2 * a[l]:
        r += 1
    ans = max(ans, r - l)
    l += 1

print(ans)
