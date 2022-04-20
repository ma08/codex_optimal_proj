

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]

    if n == 1:
        print(0)
        return

    if max(a) - min(a) > sum(a):
        print(-1)
        return

    print(max(a) - min(a))

if __name__ == "__main__":
    main()