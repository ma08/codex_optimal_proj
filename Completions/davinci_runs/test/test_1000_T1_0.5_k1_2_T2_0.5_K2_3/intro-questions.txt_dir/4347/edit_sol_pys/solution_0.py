
import math

def round_dance(n):
    return math.factorial(n) // (2 * math.factorial(n/2))

if __name__ == '__main__':
    n = int(input())
    print(round_dance(n))
