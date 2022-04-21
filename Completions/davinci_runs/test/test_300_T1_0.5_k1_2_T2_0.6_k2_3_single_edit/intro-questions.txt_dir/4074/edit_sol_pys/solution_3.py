

t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    if n < p:
        print(1)
    else:
        print(n // p + n % p)
