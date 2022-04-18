

import math

def euler(n, precision=100):
    return sum(1/math.factorial(i) for i in range(n+1)) + 10**-precision

if __name__ == '__main__':
    print(euler(int(input())))
