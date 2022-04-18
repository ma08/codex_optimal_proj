

import sys
import math

def main():
    m = int(sys.stdin.readline().strip())
    for a in range(1,m):
        for b in range(1,m):
            for c in range(1,m):
                if a**2 + b**2 == c**2 and a+b+c == m:
                    print(a*b*c)
                    return
    print(-1)
main()
