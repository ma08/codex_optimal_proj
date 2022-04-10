
a, b, c, d = map(int, input().split())  # input

if a * c <= a * d and a * c <= b * c:  # if
    print(a * c)
elif a * d <= a * c and a * d <= b * d:
    print(a * d)
elif b * c <= a * c and b * c <= b * d:
    print(b * c)
else:
    print(b * d)
