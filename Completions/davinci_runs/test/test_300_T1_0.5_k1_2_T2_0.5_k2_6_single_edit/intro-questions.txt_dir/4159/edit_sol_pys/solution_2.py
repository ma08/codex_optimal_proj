a,b,k = map(int, input().split())
if k <= a:
    print(a-k,b)
else:
    k -= a
    a = 0
    if k <= b:
        print(a,b-k)
    else:
        b = 0
        print(a,b)

