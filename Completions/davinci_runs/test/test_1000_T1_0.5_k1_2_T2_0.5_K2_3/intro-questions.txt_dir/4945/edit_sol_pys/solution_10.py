
a, b = map(int, input().split())
m, s = map(int, input().split())

if s <= 2 * m:
    print(a*m)
else:
    print(a)
