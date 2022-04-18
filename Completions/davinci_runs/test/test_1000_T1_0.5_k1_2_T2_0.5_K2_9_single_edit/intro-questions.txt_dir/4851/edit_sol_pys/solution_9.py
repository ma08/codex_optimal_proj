def sum_digits(number):
    summ = 0
    while number:
        summ += number % 10
        number //= 10
    return summ
number = int(input())
while number % sum_digits(number) != 0:
    number += 1
print(number)
