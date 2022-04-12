

import math

def round_dance(n, k):
    return math.factorial(n) // (k * math.factorial(n // k))

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(round_dance(n, k))
