

a, b, c, d = map(int, input().split())

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
    print(b-a)
elif (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d):
    print(d-c)
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
    print(b-a)
elif (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):
    print(d-c)
else:
    print(c-a)
