
def multiply_digits(n):
    if n > 9:
        return n % 10 * multiply_digits(n // 10)
    else:
        return n

n = int(input())
print(multiply_digits(n))
