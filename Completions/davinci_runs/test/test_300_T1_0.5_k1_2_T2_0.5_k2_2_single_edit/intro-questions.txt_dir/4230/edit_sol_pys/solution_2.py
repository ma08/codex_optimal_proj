n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if k >= n:
    print(0)
    exit()
print(sum(a[k:]))
