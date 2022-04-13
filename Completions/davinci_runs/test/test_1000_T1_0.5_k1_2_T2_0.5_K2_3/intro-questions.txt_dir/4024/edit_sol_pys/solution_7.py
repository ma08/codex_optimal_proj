n, k = [int(x) for x in input().split()]

if k > n or k == 0:
    print(-1)
else:
    print(n - k)
