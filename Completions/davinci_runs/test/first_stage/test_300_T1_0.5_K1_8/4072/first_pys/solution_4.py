

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

def is_prime_sum(n):
    sum_of_digits = sum([int(digit) for digit in str(n)])
    return is_prime(sum_of_digits)


if __name__ == "__main__":
    print(is_prime_sum(int(input())))