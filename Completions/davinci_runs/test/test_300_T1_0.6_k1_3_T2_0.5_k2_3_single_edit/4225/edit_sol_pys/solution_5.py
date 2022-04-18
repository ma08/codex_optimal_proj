

a, b, c = map(int, input().split())
k = int(input())

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print(a - (k - (a + b)))
