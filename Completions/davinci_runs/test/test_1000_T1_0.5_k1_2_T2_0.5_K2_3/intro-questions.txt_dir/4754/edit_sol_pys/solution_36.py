

import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    socks = sorted(socks)
    count = 0
    if len(socks) % 2 != 0:
        print("Impossible")
    else:
        for i in range(0, len(socks), 2):
            if socks[i] != socks[i+1]:
                count += 1
    if count == 0:
        print(len(socks) // 2)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
