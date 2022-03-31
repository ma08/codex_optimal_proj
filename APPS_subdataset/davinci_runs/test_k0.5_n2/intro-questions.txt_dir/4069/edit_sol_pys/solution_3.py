# input
x, k, d = map(int, input().split())

# initialization
res = 0

# process
if x < 0:
    x = -x

if k <= x // d:
    res = x - k * d
else:
    k -= x // d
    x %= d
    if k % 2 == 0:
        res = x
    else:
        res = d - x

print(res)
