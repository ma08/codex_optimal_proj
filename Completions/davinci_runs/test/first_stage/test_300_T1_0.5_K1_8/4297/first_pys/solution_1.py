

import sys

def main():
    N = int(sys.stdin.readline())
    ans = 1
    while ans % 2 != 0 or ans % N != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()