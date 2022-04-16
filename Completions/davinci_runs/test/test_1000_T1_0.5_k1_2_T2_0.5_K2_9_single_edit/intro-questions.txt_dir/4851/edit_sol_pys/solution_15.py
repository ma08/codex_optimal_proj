

def sumDigits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = int(input())

while n % sumDigits(n) != 0:
    n += 1

print(n)
