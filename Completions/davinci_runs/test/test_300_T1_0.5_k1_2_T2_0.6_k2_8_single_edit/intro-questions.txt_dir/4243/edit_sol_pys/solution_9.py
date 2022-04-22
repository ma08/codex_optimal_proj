

import sys

def max_happiness(x):
    return x // 500 * 1000 + x % 500 // 5 * 5

def main():
    x = int(sys.stdin.readline().rstrip())
    print(max_happiness(x))

if __name__ == '__main__':

    main()
