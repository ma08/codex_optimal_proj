

n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == 1:
        a[i] = 0
    else:
        a[i] = 1

count = 0
ans = 0
for i in range(n):
    if a[i] == 1:
        count += 1
    else:
        count = 0
    ans = max(ans, count)

print(ans)
