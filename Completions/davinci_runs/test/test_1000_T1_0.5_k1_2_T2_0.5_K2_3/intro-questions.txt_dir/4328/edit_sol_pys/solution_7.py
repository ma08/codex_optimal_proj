
a, b = map(int, input().split())

if a % b == 0:
    print(b - a)
    print(a + b)
else:
    print(a - b)
