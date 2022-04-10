

def sum_of_digits(n):
    """Returns the sum of digits of a number"""
    return sum(int(i) for i in str(n))

def is_interesting(n):
    """Returns True if number is interesting"""
    return sum_of_digits(n) % 4 == 0

def first_interesting_number(n):
    """Returns the first interesting number equal or greater than n"""
    while not is_interesting(n):
        n += 1
    return n

print(first_interesting_number(int(input())))