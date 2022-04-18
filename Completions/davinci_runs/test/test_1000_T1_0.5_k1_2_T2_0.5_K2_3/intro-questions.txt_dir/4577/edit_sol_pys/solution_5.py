
a, b, c, k = map(int, input().split())

if k <= a:
    print(k)
elif a < k <= a + b:
    print(a)
else: # k > a + b
    print(a - (k - a - b))
