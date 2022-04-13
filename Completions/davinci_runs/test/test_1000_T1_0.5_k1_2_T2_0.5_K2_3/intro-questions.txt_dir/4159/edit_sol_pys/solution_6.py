

a, b, k = map(int, input().split())  # input a,b,k

if k <= a:  # condition for a
    a -= k
else:
    k -= a
    a = 0
    if k <= b:  # condition for b
        b -= k
    else:
        b = 0

print(a, b)
