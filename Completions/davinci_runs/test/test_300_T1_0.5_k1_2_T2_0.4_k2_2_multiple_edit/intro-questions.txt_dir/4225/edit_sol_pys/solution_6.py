

# a, b, c, k = map(int, input().split())
a, b, c, k = 2, 1, 1, 4

if k <= a:
    print(k)
elif k <= a+b:
    print(a)
else:
    print(a - (k - a - b))
