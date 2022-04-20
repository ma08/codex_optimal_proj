

x, a, b = map(int, input().split())

if x - a >= b:
    print(b)
elif x - a < 0:
    print(0)
else:
    print(x - a)
