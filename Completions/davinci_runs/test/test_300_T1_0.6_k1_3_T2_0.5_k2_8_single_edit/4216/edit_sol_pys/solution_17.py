

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = a[::-2]
    print(' '.join(map(str, b)))

if __name__ == '__main__':
    main()
