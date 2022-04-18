
from collections import defaultdict
from itertools import product


def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a_divisors = defaultdict(set)
    for a_i in a:
        for divisor in get_divisors(a_i):
            a_divisors[divisor].add(a_i)
    b_divisors = defaultdict(set)
    for b_i in b:
        for divisor in get_divisors(b_i):
            b_divisors[divisor].add(b_i)
    result = 0
    for divisor in a_divisors.keys():
        if divisor in b_divisors:
            result += len(a_divisors[divisor]) * len(b_divisors[divisor])
    print(result)


if __name__ == '__main__':
    main()
