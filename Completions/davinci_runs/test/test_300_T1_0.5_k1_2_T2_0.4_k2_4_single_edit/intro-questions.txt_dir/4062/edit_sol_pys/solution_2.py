

a, b, c, d = map(int, input().split())

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
    print(b * d - a * d - a * c + c * d)
elif (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d):
    print(b * d - a * d - a * c + c * d)
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
    print(b * d - a * d - a * c + c * d)
elif (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):
    print(b * d - a * d - a * c + c * d)
else:
    print(b * d - a * d - a * c + c * d)
