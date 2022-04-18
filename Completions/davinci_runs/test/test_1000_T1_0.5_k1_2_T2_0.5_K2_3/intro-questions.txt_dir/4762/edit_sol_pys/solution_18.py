

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main(P):
    N = int(P[0]) # Number of people
    prob = float(factorial(N-1)) / float(N**N) # Probability of having a birthday
    print(prob) # Print the probability

if __name__ == "__main__":
    main(sys.stdin.readlines())
