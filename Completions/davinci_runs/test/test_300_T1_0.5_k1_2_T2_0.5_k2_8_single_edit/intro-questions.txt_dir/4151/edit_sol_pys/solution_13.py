

import sys, math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def main():
    n, m = map(int, input().split())
    if n >= m:
        print(n - m)
        exit()
    if m % n == 0:
        print(0)
        exit()
    divisors = get_divisors(m)
    divisors.sort()
    print(min(divisors[i] - divisors[i - 1] for i in range(1, len(divisors))))


if __name__ == '__main__':
    main()
