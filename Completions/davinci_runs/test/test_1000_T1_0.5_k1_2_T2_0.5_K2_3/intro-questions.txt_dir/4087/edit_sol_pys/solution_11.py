

a = int(input())


def get_sum_of_digits(n):
    return sum(map(int, str(n)))


def is_interesting(n):
    if get_sum_of_digits(n) % 4 == 0:
        return True

    return False

def get_next_interesting(number):
    if is_interesting(number):
        return number
    for i in range(number, number*10):
        if is_interesting(i):
            return i


print(get_next_interesting(a))
