
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

def is_prime_sum(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def main():
    n = int(input())
    if is_prime_sum(n):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
