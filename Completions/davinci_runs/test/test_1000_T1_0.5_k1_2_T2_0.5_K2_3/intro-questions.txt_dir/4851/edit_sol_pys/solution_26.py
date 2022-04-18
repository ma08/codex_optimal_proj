def sum_digits(n):
    return sum(int(x) for x in str(n))

n = int(input())

while n % sum_digits(n) != 0:

    n += 1
print(n)
