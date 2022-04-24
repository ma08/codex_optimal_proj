
a,b,c = map(int, input().split())

if c <= a:
    a -= c
else:
    c -= a
    a = 0
    if c <= b:
        b -= c
    else:
        b = 0

print(a,b)
