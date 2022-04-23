
def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    while True:
        if x == 3:
            return True
        if x == 5:
            return True
        if x == 7:
            return True
        if x == 11:
            return True
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
            return False
        else:
            return True
