
def multiply_digits(n):
    if n < 10:
        return n
    return n % 10 * multiply_digits(n // 10)

if __name__ == "__main__":
    n = int(input())
    print(multiply_digits(n))
