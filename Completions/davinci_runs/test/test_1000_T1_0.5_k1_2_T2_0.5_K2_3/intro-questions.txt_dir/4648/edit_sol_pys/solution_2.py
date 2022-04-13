

# cook your dish here.
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(0)
        continue
    if n % 6 == 0:
        count = 0
        while n > 1:
            if n % 6 == 0:
                n //= 6
            else:
                n *= 2
            count += 1
        print(count)
    else:
        print(-1)
