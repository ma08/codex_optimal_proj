

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main(N):
    prob = float(factorial(N-1)) / float(N**N) * 100
    print("{:.2f}".format(prob))

if __name__ == "__main__":
    main(int(sys.stdin.readlines()[0]))
