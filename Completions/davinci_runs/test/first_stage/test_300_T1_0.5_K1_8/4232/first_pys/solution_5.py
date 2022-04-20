

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if n - k < k:
    k = n - k

if k == 0:
    print(a[-1])
else:
    print(a[k - 1])