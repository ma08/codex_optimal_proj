

import sys

def main():
    n = [int(x) for x in sys.stdin.readline().split()]
    print(sum(n) % 2)

if __name__ == '__main__':
    main()