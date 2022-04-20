
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return sum_of_digits(number // 10) + number % 10
print(sum_of_digits(int(input())))
