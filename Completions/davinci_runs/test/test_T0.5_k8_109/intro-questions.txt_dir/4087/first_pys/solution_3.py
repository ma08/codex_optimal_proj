

a = int(input())

def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

while sumDigits(a) % 4 != 0:
    a += 1

print(a)