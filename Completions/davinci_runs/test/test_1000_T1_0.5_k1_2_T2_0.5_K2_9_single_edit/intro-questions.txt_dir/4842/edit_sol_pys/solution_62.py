

import sys

def main():
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        v = list(map(int, f.readline().strip().split()))

def main():
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    print_diff_table(n, v)

if __name__ == '__main__':
    main()
