import sys
import math

def calc_fac(n):
    if n == 0:
        return 1
    else:
        return n * calc_fac(n-1)

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())
    print(calc_fac(N) // (calc_fac(N-M)*calc_fac(M)))

main()
