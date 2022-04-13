n, x = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(n-1):
    if a[i] + a[i+1] > x:
        count += a[i] + a[i+1] - x
        a[i+1] -= a[i] + a[i+1] - x if a[i] + a[i+1] - x < a[i+1] else a[i+1]
print(count)
