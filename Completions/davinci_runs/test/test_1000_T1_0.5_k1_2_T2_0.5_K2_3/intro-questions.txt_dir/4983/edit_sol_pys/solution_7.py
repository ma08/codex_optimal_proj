

def multiply_digit(n):
    if n > 9:
        n = n % 10 * multiply_digit(n // 10) # recursive call
    return n

n = int(input())
print(multiply_digit(n))
