

a, b = map(int, input().split())

if a % b == 0:
    print(b - a, a + b)
else:
    print(a - b, a + b)
