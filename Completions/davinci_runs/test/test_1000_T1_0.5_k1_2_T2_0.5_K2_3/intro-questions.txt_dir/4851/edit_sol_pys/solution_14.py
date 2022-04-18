
n = int(input())  # вводимо число


def sum_digits(n):  # сума цифр в числі
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


while n % sum_digits(n) != 0:  # закидуємо число в цикл щоб знайти найменше просте число, яке ділиться на суму цифр
    n += 1
print(n)
