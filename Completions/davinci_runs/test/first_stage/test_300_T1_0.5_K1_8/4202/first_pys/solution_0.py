

import sys

def main():
    l, r = map(int, sys.stdin.readline().split())
    if l == 0:
        print(0)
        return

    min_i = l // 2019
    min_j = (l + 2019 - 1) // 2019
    if min_i == min_j:
        print(0)
    else:
        print(min_i * min_j % 2019)

if __name__ == '__main__':
    main()