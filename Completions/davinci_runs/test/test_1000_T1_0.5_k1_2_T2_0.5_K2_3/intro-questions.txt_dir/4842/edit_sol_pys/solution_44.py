
import sys
import math

def main():
    n = int(sys.stdin.readline())
    v = [int(x) for x in sys.stdin.readline().split()]
    d = 0
    for i in range(n-1):
        if v[i+1] - v[i] != v[i+2] - v[i+1]:
            d = i+2
            break
    print(d, v[d-1] + v[d] - v[d-2])

main()
