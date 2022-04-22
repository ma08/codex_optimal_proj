

def main():
    # read input
    n = int(input())
    s = input()

    # calculate minimum prime number
    ans = 0
    for i in range(n):
        if s[i] == 'R':
            ans += 1

    # calculate minimum prime number
    prime_num = x
    while True:
        if is_prime(prime_num):
            break
        else:
            prime_num += 1

    # output
    print(prime_num)

def is_prime(n):
    """
    Check if n is prime.
    """
    if n == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    main()
