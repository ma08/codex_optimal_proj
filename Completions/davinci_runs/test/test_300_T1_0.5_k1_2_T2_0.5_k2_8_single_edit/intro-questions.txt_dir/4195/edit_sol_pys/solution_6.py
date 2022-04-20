

d, n = map(int, input().split())
if n == 1:
    print(100)
    exit()


if d == 0:
    print(100**n)
else:
    print(101**n)
