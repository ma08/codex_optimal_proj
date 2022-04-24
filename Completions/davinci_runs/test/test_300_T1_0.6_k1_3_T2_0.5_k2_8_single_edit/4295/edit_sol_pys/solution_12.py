

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    print(min(N % K, abs(N % K - K)))

if __name__ == '__main__':
    main()
