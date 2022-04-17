import math

import sys

def main():
    line = sys.stdin.readline().split()
    n = int(line[0])
    k = int(line[1])
    if k == 0:
        print(n)
        return
    count = 0
    for i in range(1, n + 1):
        if (n % i) == 0:
            count += 1
            if count == k:
                print(i)
                return
    print(-1)


if __name__ == '__main__':
    main()
