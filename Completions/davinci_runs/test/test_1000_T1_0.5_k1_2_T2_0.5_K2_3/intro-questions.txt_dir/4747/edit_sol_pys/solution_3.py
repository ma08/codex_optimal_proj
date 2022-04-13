

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    print(calc_expected_score(n, k))

def calc_expected_score(n, k):
    if k == 1:
        return n / 2
    else:
        numerator = 0
        for i in range(1, n+1):
            numerator += i * (k - 1) / (n ** k)
        return numerator

if __name__ == "__main__":
    main()
