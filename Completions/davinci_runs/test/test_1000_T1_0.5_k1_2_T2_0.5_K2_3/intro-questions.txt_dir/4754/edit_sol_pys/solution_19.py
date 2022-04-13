

import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = sorted([int(x) for x in sys.stdin.readline().strip().split()])
    count = 0
    for i in range(0, len(socks)-1, 2):
        if socks[i] != socks[i+1] or socks[i] == socks[i+1]:
            count += 1
    if count == 0 or count == 1:
        print(len(socks) // 2)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
