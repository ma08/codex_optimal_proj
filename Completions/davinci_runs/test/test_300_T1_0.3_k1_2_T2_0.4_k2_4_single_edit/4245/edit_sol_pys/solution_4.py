

import sys

def main():
    line = sys.stdin.readline().rstrip()
    N, K = map(int, line.split())
    print(K // N + (K % N != 0))

if __name__ == '__main__':
    main()
