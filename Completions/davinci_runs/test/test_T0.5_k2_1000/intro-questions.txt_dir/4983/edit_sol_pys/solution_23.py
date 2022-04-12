
def multiply_digits(n: int) -> int:
    if n > 9:
        n = (n % 10) * multiply_digits(n // 10)
    return n


n = int(input())
print(multiply_digits(n))
