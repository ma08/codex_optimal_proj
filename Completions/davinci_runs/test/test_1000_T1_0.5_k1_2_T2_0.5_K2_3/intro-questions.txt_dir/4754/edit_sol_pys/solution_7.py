
import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = list(map(int, sys.stdin.readline().strip().split()))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if socks[i] == socks[j]:
                count += 1
                socks[i] = -1
                socks[j] = -1
                break
    print(count)

if __name__ == "__main__":
    main()
