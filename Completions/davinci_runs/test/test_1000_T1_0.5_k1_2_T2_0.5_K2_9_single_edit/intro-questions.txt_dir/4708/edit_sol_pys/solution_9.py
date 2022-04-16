
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0:
    print(b)
elif b == 0:
    print(a)
elif c == 0:
    print(d)
elif d == 0:
    print(c)
elif a == c:
    print(d)
elif b == d:
    print(c)
elif a == d:
    print(b)
elif b == c:
    print(a)
