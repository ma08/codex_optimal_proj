
def sum_digits(n):  # define function
    sum = 0  # define sum
    while n > 0:
        sum += n % 10  # add last digit to sum
        n //= 10  # remove last digit
    return sum

n = int(input())

while n % sum_digits(n) != 0:
    n += 1

print(n)
