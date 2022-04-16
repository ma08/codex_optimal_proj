
a,b,k = map(int, input().split())

if k <= a:
    a -= k
else:
    k -= a
    if k <= b:
        b -= k
    else:
        b -= k

print(a,b)
