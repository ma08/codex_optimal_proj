

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().rstrip().split())
    ans = 0
    if n < a + b:
        ans = 0
    elif a == b:
        ans = n - a
    else:
        ans = n
        if a < b:
            tmp = a
            a = b
            b = tmp
        ans -= a
        k = (a - b)
        ans -= k * ((ans - 1) // k)
    print(ans)


if __name__ == '__main__':
    main()
