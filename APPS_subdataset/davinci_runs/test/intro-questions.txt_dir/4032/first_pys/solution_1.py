

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = 0
while len(a) > 0:
    if a[0] <= k:
        a = a[1:]
        ans += 1
    elif a[-1] <= k:
        a = a[:-1]
        ans += 1
    else:
        break
print(ans)