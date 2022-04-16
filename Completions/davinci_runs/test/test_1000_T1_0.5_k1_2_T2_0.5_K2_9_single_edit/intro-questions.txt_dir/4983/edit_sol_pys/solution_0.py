

def multiply_digits(number):
    if number > 9:
        number = number % 10 * multiply_digits(number // 10)
    return number

n = int(input())
print(multiply_digits(n))
