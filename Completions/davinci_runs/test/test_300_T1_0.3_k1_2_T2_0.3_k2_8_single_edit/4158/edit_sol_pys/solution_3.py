
n = int(input())
x = list(map(int, input().split()))

x.sort()

d = {}
for i in range(n-1):
    for j in range(i+1, n-1):
        d[x[j+1] - x[i]] = d.get(x[j+1] - x[i], 0) + 1

ans = []
for i in range(n-1):
    for j in range(i+1, n-1):
        if d.get(x[j+1] - x[i], 0) > 1:
            ans.append(x[i])
            ans.append(x[j+1])
            d[x[j+1] - x[i]] -= 2

print(len(ans))
print(*ans)
