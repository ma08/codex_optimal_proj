
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main(P):
    N = int(P[0])
    prob = float(factorial(N-1)) / float(N**N)
    print(prob)

if __name__ == "__main__":
    main(sys.stdin.readlines())
