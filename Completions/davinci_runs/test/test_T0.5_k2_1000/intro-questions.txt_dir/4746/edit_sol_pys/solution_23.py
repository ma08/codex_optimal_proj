

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Znajdź największą liczbę naturalną n, która spełnia następujące warunki:

1. n jest liczbą pierwszą
2. n + 1 jest liczbą pierwszą
3. n + 2 jest liczbą pierwszą
4. n + 3 jest liczbą pierwszą

"""

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main(args):
    n = 2
    while True:
        if is_prime(n) and is_prime(n + 1) and is_prime(n + 2) and is_prime(n + 3):
            print(n)
            return 0
        n += 1
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
