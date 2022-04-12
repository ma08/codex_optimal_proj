

import sys

def main():
    n = int(sys.stdin.readline())
    print(calc_expected_score(n))

def calc_expected_score(n):
    numerator = 0
    for i in range(1, n+1):
        numerator += i * (n-1) / (n**n - 1)
    return numerator

if __name__ == "__main__":
    main()
