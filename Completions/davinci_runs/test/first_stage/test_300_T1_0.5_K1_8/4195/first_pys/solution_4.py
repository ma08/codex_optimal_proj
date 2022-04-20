

import sys

def main():
    d, n = [int(i) for i in sys.stdin.readline().split()]
    if d == 0:
        print(n)
    elif d == 1:
        print(n*100)
    else:
        print(n*10000)

if __name__ == '__main__':
    main()