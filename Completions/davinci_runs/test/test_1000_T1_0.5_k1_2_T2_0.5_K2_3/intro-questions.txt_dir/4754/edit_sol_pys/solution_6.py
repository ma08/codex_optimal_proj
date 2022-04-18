
import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = [int(x) for x in sys.stdin.readline().strip().split()]
    socks = sorted(socks)
    count = 0
    i = 0
    while i < len(socks):
        if socks[i] != socks[i+1] and socks[i] != socks[i+2]:
            count += 1
            i += 1
        else:
            i += 2

    if count == 0:
        print(len(socks) // 2)
    else:
        print("impossible")

if __name__ == "__main__":
    main()
