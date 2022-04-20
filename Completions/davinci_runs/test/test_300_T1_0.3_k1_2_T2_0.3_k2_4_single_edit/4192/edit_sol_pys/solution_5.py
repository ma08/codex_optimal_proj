

d, t, s = map(float, input().split())

if d / s <= t or d % s == 0:
    print('Yes')
else:
    print('No')
