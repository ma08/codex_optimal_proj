

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
count = 1

for i in range(n - 1):
    if a[i] < a[i + 1]:
        count += 1
    else:
        ans += count // k
        count = 1

if count != 1:
    ans += count // k

print(ans)
