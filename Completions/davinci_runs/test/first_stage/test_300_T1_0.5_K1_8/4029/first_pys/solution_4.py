

import sys

def main():
    n = int(input())
    if n % 25 == 0:
        print(0)
    else:
        print(check(n, 0))

def check(n, c):
    if n % 25 == 0:
        return c
    else:
        if len(str(n)) < 3:
            return -1
        else:
            return min(check(swap(n, i), c+1) for i in range(len(str(n))-1))

def swap(n, i):
    n = str(n)
    n = n[:i] + n[i+1] + n[i] + n[i+2:]
    return int(n)

if __name__ == '__main__':
    main()