

a, b, c = [int(x) for x in input().split()]

if a <= b and a <= c:
    print(a + min(b, c))
elif b <= a and b <= c:
    print(b + min(a, c))
else:
    print(c + min(a, b))