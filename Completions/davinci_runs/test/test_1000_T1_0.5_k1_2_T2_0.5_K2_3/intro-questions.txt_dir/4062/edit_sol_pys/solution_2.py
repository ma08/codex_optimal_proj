

a, b, c, d = map(int, input().split())  # input 4 numbers

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d) or (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d) or (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b) or (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):
    print(max(a, c) * max(b, d))
else:
    print(min(a, c) * min(b, d))
