

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

l, r = 0, n - 1
ans = 0

while l <= r:
    if a[l] <= k:
        l += 1
        ans += 1
    elif a[r] <= k:
        r -= 1
        ans += 1
    else:
        break

print(ans)