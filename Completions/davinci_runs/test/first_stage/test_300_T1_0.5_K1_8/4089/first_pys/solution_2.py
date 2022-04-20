

import sys

def main():
    n = int(sys.stdin.readline())
    num = n-1
    s = ""
    while num >= 0:
        s = chr(ord('a') + num % 26) + s
        num = num // 26 - 1
    print(s)

if __name__ == '__main__':
    main()