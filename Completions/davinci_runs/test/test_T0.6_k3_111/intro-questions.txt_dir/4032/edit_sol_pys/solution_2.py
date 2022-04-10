n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
left, right = 0, n - 1
while left <= right:
    if a[left] <= k:
        ans += 1
        left += 1
    elif a[right] <= k:
        ans += 1
        right -= 1
    else:
        break
print(ans)
