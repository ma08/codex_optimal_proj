#

n, h, l, r = map(int, input().split())
a = [int(i) for i in input().split()]

if l == 0:
    if r == h - 1:
        print(n)
    else:
        print(n - 1)
else:
    t = 0
    c = 0
    for i in range(n):
        t += a[i]
        if l <= t % h <= r:
            c += 1
    print(c)
