

import sys

def max_allocation(a, b, c):
    return max(a+b+c, a*10+b+c, a+b*10+c, a*10+b*10+c, (a+b)*10+c, a*10+(b+c), a*100+b+c, a+b*100+c, a*100+b*100+c, a*100+b+c*100)

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    print(max_allocation(a, b, c))
