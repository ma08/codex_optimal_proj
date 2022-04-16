

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    print(calc_expected_score(n, k))

def calc_expected_score(n, k):
    if k == 1:
        return n/2 + 0.5 # expected score of a single die
    else:
        expected_score = 0
        for i in range(1, n+1):
            expected_score += i * (k-1) / (n**k - 1)
        return expected_score

if __name__ == "__main__":
    main()
