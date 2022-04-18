

import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    socks = sorted(socks)
    print(len(socks) // 2)


if __name__ == "__main__":
    main()
