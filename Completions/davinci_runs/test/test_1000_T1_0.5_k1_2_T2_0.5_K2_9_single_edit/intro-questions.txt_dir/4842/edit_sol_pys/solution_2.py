

import sys
import math

def main():
    n = int(sys.stdin.readline())
    v = [int(x) for x in sys.stdin.readline().split()]
    d = 0
    for i in range(n-1):
        if v[i+1] - v[i] != v[i+2] - v[i+1]: # find the different element
            d = i+2 # d is the number of the different element
            break
    print(d, v[n-1] + v[1] - v[0])

main()
