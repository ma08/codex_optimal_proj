

# Solution

n, r = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[1])

ans = 0

for i in range(n):
    if r >= a[i][0]:
        ans += 1
        r += a[i][1]

print(ans)