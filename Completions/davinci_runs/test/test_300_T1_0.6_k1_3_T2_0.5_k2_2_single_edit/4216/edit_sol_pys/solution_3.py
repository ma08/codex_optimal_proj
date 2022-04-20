

def check_if_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_if_palindrome(n):
    return str(n) == str(n)[::-1]

def check_if_emirp(n):
    return check_if_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_palindrome_prime(n):
    return check_if_prime(n) and check_if_palindrome(n)

def check_if_emirp_palindrome(n):
    return check_if_emirp(n) and check_if_palindrome(n)

def check_if_emirp_palindrome_prime(n):
    return check_if_emirp_palindrome(n) and check_if_prime(n)

def check_if_emirp_palindrome_prime_reversed(n):
    return check_if_emirp_palindrome_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n) and check_if_prime(int(str(n)[::-1]))

def check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed(n):
    return check_if_emirp_palindrome_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime_reversed_prime(n) and check_if_prime(int(str(n)[::-1]))
