

a, b, c, d = map(int, input().split())

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
    print(abs(a - b) * abs(c - d))
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
    print(abs(a - b) * abs(c - d))
else:
    print(abs(a - c) * abs(b - d))
