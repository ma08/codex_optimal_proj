

def multiply_digit(n):
    if n > 9 and n != 0:
        n = n % 10 * multiply_digit(n // 10)
    return n

n = int(input())
print(multiply_digit(n))
