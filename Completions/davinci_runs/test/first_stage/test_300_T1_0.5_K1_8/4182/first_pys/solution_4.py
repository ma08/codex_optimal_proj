

import sys

def main():
    N, M, X, Y = [int(x) for x in sys.stdin.readline().split()]
    x = [int(x) for x in sys.stdin.readline().split()]
    y = [int(x) for x in sys.stdin.readline().split()]
    if X >= Y or max(x) >= min(y):
        print('War')
    else:
        print('No War')

if __name__ == '__main__':
    main()