

import sys

def main():
    a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    print(max(b, d) * max(b, d))

if __name__ == '__main__':
    main()
