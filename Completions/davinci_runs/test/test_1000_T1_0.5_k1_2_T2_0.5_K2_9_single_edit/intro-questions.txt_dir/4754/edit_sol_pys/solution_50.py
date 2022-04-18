

import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    socks = sorted(socks)
    count = 0
    for i in range(len(socks) - 1):
        if socks[i] == socks[i+1]:
            socks.pop(i)
            socks.pop(i)
            count += 2
    print(count)

if __name__ == "__main__":
    main()
