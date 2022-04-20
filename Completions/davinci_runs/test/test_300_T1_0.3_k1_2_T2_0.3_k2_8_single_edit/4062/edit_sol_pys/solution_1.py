
a, b, c, d = map(int, input().split()) # a, b, c, d = (int(input()) for _ in range(4))

if a * c >= a * d and a * c >= b * c and a * c >= b * d:
    print(a * c)
elif a * d >= a * c and a * d >= b * c and a * d >= b * d:
    print(a * d)
elif b * c >= a * c and b * c >= a * d and b * c >= b * d:
    print(b * c)
elif b * d >= a * c and b * d >= a * d and b * d >= b * c:
    print(b * d)
