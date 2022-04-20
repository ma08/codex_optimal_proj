

import sys

def main():
    n, b, a = map(int, sys.stdin.readline().split())
    s = map(int, sys.stdin.readline().split())
    l = 0
    for i in range(n):
        if s[i] == 1:
            if b < a:
                b += 1
            else:
                a -= 1
        if a > 0:
            a -= 1
        elif b > 0:
            b -= 1
        else:
            break
        l += 1
    print l

if __name__ == '__main__':
    main()