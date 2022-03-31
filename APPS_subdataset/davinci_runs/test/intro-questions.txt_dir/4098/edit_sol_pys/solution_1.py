n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()

if k == 1:
    print(n)
elif k == n:
    print(1)
else:
    b = []
    for i in range(n-1):
        b.append(a[i+1] - a[i])
    b.sort()
    s = sum(b[:n-k+1]) + n
    print(s)
