n, x, t = map(int, input().split(" "))

if n % x == 0:
    print(t * (n // x) + t)
else:
    print(t * (n // x + 1) + t)
