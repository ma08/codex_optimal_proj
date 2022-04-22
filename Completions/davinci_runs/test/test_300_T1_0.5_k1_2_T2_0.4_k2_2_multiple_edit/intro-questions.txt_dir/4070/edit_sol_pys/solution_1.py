import sys

def prime_sieve(n):
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def solve(n):
    if n <= 2:
        return 0
    elif n == 3:
        return 1
    else:
        prime_lst = []
        for i in range(2, n):
            if check_prime(i):
                prime_lst.append(i)
        count = 0
        for i in prime_lst:
            if i + 2 in prime_lst:
                count += 1
        return count


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))
