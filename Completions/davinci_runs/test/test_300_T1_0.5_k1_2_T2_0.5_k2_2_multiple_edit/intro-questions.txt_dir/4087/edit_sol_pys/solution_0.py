

a = int(input())
# a = 99

# a = 99
# a = 237

# a = 42

def get_sum_of_digits(num):
    return sum(map(int, str(num)))

def is_interesting(num):
    if get_sum_of_digits(num) % 4 == 0:
        return True
    return False

def get_next_interesting(num):
    if is_interesting(num):
        return num
    for i in range(num, num*10):
        if is_interesting(i):
            return i

print(get_next_interesting(a))
