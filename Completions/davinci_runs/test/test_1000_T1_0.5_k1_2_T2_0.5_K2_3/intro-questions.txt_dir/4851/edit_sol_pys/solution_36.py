

def sum_digits(n):
    sum_ = 0
    while n > 0:
        sum_ += n % 10
        n //= 10
    return sum_

n = int(input())

while n % sum_digits(n) != 0:
    n += 1

print(n)
