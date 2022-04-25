

n, h, l, r = map(int, input().split()) # n = number of days, h = hours in a day, l = left bound, r = right bound
a = list(map(int, input().split())) # this is a list of the number of hours slept each night

if l == 0:
    if r == h - 1:
        print(n)
    else:
        print(n-1)
else:
    t = 0
    c = 0
    for i in range(n):
        t += a[i]
        if l <= t % h <= r:
            c += 1
    print(c)
