
n = int(input())
if n > 9:
    m = 1
    while n > 9:
        p = n % 10
        if p > 0:
            m *= p
        n //= 10
    print(m * n)
else:
    print(n)
