

import sys

def main():
    n, k = sys.stdin.readline().split()
    n = int(n)
    k = int(k)

    print(calculate(n, k))

def calculate(n, k):
    if k == 1:
        return (n + 1)/2
    else:
        return (n + 1)/2 + ((n - 1)/n)*(k - 1)*calculate(n, k - 1)

main()
