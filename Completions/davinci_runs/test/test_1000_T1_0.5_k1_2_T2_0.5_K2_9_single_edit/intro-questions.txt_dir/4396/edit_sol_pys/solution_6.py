

import sys

def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            total += float(x)
        else:
            total += float(x) * 380000.0
    print(total)
    return

if __name__ == '__main__':
    main()
