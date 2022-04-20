

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_prime_sum(n, k):
    if is_prime(n):
        return False
    for i in range(2, n//2):
        if is_prime(i) and is_prime(n - i) and k == 1:
            return True, i, n-i
        elif is_prime(i) and is_prime(n - i):
            return is_prime_sum(n - i, k - 1)
    return False

def main():
    n = int(input())
    k = int(input())
    if is_prime_sum(n, k):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
