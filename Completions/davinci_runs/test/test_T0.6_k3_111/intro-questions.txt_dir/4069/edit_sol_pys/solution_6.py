x, k, d = map(int,input().split())

if k*d > abs(x):
    k = abs(x) // d
    x -= k*d
    if abs(x) % d == 0:
        print(abs(x))
    else:
        print(abs(x) - d)
else:
    print(abs(x - k*d))
