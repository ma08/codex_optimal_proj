
n,h,l,r = map(int, input().split())
a = list(map(int, input().split()))

if l == 0 and r == h-1:
        print(n)
else:
    t = 0
    c = 0
    for i in range(n):
        t += a[i]
        if l <= t%h <= r:
            c += 1
    print(c)
