

import sys
import math

def main():
    m = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    x = 0
    y = 0
    for i in range(n):
        a,b = map(int,sys.stdin.readline().strip().split())
        x += a
        y += b
    print(str(x//m) + " " + str(y//m))

main()
