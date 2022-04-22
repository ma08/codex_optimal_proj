

a, b, c, d = map(int, input().split())

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
    print(max(b, d) - min(a, c))
elif (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d):
    print(max(b, d) - min(a, c))
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
    print(max(b, d) - min(a, c))
elif (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):
    print(max(b, d) - min(a, c))
else:
    print(max(a, c) - min(b, d))
