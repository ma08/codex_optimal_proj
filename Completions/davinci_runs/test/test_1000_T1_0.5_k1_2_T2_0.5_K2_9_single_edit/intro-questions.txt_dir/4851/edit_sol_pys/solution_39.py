
def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

n = int(input())

while n % sumDigits(n) != 0:
    n += 1

print(n)
