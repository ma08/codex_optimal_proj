

import sys

def main():
    num_tests = int(sys.stdin.readline())
    for i in range(num_tests):
        n, k = map(int, sys.stdin.readline().split())
        if n % k == 0:
            print(n // k)
        else:
            print(n // k + 1)

if __name__ == '__main__':
    main()