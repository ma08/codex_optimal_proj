import sys

import sys

def main():
    num = int(sys.stdin.readline().strip())
    res = 0

    while num > 0:
        res = res << 1
        res = res | (num & 1)
        num = num >> 1

    print(res)

if __name__ == '__main__':
    main()
