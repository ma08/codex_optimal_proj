

a, b, c, d = map(int, input().split())

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
    print(abs(b - c) * abs(d - a))
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
    print(abs(b - c) * abs(d - a))
else:
    print(abs(b - d) * abs(c - a))
