

import sys

def main():
    D, N = map(int, input().split())
    if D == 0:
        print(N)
    else:
        print(100 * N)

if __name__ == '__main__':
    main()