
n = int(input())

def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum

while n % sum_digits(n) != 0:
    n += 1
print(n)
