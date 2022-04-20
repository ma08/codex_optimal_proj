
k -= a
a,b,k = map(int, input().split())

if k <= a:
    a -= k
else:
    a = 0
    if k <= b:
        b -= k
    else:
        b = 0

print(a,b)
