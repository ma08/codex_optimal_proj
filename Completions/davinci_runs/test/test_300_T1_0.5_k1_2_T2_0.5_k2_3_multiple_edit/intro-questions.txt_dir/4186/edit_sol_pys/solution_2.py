

n = int(input())
a = list(map(int, input().split()))
a.sort()
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

ans = 0
for i in d:
    if d[i] > 2:
        ans += d[i] - 2

print(ans)
