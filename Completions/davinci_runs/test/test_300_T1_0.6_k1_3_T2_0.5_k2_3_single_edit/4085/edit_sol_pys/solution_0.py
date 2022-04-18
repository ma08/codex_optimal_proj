
from functools import reduce
import math

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        l = [int(x) for x in input().split()]
        l.sort()
        ans = reduce(math.gcd, l)
        if ans > 1:
            print(ans)
        else:
            print(-1)

if __name__ == '__main__':
    main()
