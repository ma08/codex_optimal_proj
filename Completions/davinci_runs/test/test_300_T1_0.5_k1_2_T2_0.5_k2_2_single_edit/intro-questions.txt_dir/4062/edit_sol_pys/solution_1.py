

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):
    print(b * d)
elif (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d):
    print(b * d)
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):
    print(b * d)
elif (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):
    print(b * d)
else:
    print(a * c)
