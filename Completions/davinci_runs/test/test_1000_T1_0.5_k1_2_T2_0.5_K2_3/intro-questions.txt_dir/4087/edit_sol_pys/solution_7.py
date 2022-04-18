

a = int(input())
# a = 99

def get_sum_of_digits(number):
    return sum(map(int, str(number)))

def is_interesting(number):
    if get_sum_of_digits(number) % 4 == 0:
        return True
    return False

def get_next_interesting(number):
    if is_interesting(number):
        return number
    for i in range(number, number*10):
        if is_interesting(i):
            return i

print(get_next_interesting(a))
