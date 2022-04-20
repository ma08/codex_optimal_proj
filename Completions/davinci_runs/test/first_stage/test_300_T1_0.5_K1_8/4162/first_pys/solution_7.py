

import sys

def main():
    # Read in N and array of a_i's
    N = int(input())
    a_i = [int(x) for x in sys.stdin.readline().split()]

    # Calculate the LCM of all a_i's
    lcm = a_i[0]
    for i in range(1, N):
        lcm = lcm * a_i[i] // gcd(lcm, a_i[i])
    
    # Calculate the sum of modulos of LCM / a_i
    f = 0
    for i in range(N):
        f += lcm // a_i[i]

    # Print f
    print(f)

def gcd(x, y):
    """Returns the greatest common divisor of x and y"""
    while y != 0:
        x, y = y, x % y
    return x

if __name__ == '__main__':
    main()