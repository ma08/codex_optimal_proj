
n = int(input())
a = list(map(int, input().split()))
if n == 2:
    print(0)
    a.sort()
else:
    print(min(a[n - 2] - a[0], a[n - 1] - a[1]))
