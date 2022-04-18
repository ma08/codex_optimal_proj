
n, x = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(n-1):
    if a[i] + a[i+1] > x:
        count += a[i] + a[i+1] - x
        a[i+1] -= a[i] + a[i+1] - x
print(count)
