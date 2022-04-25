
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if n == k:
        print(a[-1])
    else:
        print(a[k-1])
