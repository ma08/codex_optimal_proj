

a, b, c, d = map(int, input().split())

if (a <= c <= b or c <= a <= d) and (a <= d <= b or c <= b <= d):
    print(max(b, d))
elif (c <= a <= d or a <= c <= b) and (a <= d <= b or c <= b <= d):
    print(max(b, d))
elif (c <= a <= d or a <= c <= b) and (a <= b <= d or c <= d <= b):
    print(max(b, d))
elif (a <= c <= b or c <= a <= d) and (c <= d <= b or a <= d <= b):
    print(max(b, d))
else:
    print(a * c)
