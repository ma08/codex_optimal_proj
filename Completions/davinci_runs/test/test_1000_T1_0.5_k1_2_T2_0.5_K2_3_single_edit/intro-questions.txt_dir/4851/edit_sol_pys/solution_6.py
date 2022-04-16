

def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10  # add last digit to sum
        n //= 10  # remove last digit from n
    return sum

n = int(input())

while n % sumDigits(n) != 0:  # while n is not divisible by the sum of its digits
    n += 1  # increase n by 1

print(n)
