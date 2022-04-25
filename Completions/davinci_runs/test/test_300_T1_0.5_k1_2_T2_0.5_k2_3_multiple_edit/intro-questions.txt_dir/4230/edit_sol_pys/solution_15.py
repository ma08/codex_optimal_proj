a, b = map(int, input().split())
c, d = map(int, input().split())

if a <= c and b >= d:
    print(0)
elif a <= c and b <= d:
    print(d-b)
elif a >= c and b >= d:
    print(a-c)
else:
    print(a-c + d-b)
