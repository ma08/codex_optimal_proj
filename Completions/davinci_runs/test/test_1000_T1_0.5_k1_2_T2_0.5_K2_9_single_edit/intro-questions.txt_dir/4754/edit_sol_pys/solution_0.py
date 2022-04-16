

import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    socks = sorted(socks)
    count = 0
    i = 0
    while i < len(socks) - 1:
        if socks[i] == socks[i+1]:
            i += 2
            count += 1
        else:
            i += 1
    print(count)

if __name__ == "__main__":
    main()
