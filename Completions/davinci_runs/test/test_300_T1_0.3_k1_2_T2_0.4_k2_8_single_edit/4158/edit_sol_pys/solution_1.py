
n = int(input())
a = list(map(int, input().split()))

a.sort()

d = {}
for i in range(n):
    for j in range(i+1, n):
        d[a[j] - a[i]] = d.get(a[j] - a[i], 0) + 1

ans = []
for i in range(n):
    for j in range(i+1, n):
        if d.get(a[j] - a[i], 0) > 1:
            ans.append(a[i])
            ans.append(a[j])
            d[a[j] - a[i]] -= 2

print(len(ans))
print(*ans)
