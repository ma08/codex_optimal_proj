

import sys

def main():
    args = sys.stdin.readline().rstrip().split()
    a, b, c = map(int, args)
    print(min(b//a, c))

if __name__ == '__main__':
    main()