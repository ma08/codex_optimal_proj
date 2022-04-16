

def sumDigits(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ

n = int(input())

while n % sumDigits(n) != 0:
    n += 1

print(n)
