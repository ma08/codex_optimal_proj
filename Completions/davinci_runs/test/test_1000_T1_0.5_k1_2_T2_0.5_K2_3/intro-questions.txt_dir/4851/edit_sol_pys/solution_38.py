
# Get the sum of the digits of a number
def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r
