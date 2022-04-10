n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    if i == 0:
        ans += a[i]
    else:
        ans += min(a[i], b[i-1])
    ans += b[i]
    if i != n-1:
        ans += min(b[i], c[i])
    else:
        ans += c[i]
print(ans)
