

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    mx = max(a)
    mn = min(a)
    print(mx-mn if mx-mn != 0 else mx-1)

if __name__ == '__main__':
    main()