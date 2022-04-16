

def count(h):
    c = 0
    for i in range(1, h+1):
        c += (2*i - 1)
    return c

h, n, m = map(int, input().split())

a = count(h)

if a <= n:
    print(0, m)
else:
    a -= n
    if a <= m*2:
        print(a//2, m - (a//2))
    else:
        print(m, 0)
