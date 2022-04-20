

from sys import stdin
import math

def main():
    n = int(stdin.readline())
    ans = 0
    while n > 0:
        if n >= 9:
            n -= 9
            ans += 1
        elif n >= 6:
            n -= 6
            ans += 1
        else:
            n -= 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()