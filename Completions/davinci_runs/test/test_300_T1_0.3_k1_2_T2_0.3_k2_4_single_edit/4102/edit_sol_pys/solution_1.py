
"""
This is a sample python file
"""
def is_prime(n):
    """
    This is a sample function
    """
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
    """
    This is a sample function
    """
        if n % divisor == 0:
            return False
    return True

def is_prime_sum(n):
    if is_prime(n):
        return False
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return True
    return False

def main():
    """
    This is a sample function
    """
    n = int(input())
    if is_prime_sum(n):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
