

import sys

def main():
    K = int(sys.stdin.readline())
    n = 0
    while True:
        n += 1
        if (7 * 10**n) % K == 0:
            print(n + 1)
            break

if __name__ == '__main__':
    main()