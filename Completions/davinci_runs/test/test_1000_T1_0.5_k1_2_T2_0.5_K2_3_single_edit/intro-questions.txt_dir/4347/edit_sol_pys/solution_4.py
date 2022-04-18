
import math

def round_dances(n):
    return math.factorial(n) / (2 * math.factorial(n // 2))

if __name__ == '__main__':
    n = int(input())
    print(round_dances(n))
