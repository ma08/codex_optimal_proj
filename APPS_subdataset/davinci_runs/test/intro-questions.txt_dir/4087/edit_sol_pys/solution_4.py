

def sum_of_digits(n):  # сумма цифр числа
    s = 0
    while n:
        s += n % 10
        n //= 10

    return s

def is_interesting(n):  # проверка на кратность 4

    return sum_of_digits(n) % 4 == 0

def next_interesting(n):  # поиск следующего числа
    while not is_interesting(n):
        n += 1
    return n


if __name__ == "__main__":
    n = int(input())
    print(next_interesting(n))
