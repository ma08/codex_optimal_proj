
n = int(input())

def get_sum_of_digits(n):
    return sum(map(int, str(n)))

def is_interesting(n):
    if get_sum_of_digits(n) % 4 == 0:
        return True
    return False

def get_next_interesting(n):
    if is_interesting(n):
        return n
    for i in range(n+1, n*10):
        if is_interesting(i):
            return i

print(get_next_interesting(n))
