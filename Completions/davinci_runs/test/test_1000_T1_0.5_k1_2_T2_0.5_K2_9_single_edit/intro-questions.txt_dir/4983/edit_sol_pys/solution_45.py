

def add_digits(number):
    if number > 9:
        number = number % 10 + add_digits(number // 10)
    return number

number = int(input())
print(add_digits(number))
