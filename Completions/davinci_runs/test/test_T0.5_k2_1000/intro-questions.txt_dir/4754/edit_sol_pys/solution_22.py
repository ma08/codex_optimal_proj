
import sys

def main():
    n = int(sys.stdin.readline().strip())
    socks = list(map(int, sys.stdin.readline().strip().split()))

    count = 0
    # Count number of socks for each type
    socks_count = {}
    for sock in socks:
        socks_count[sock] = socks_count.get(sock, 0) + 1
    # Count number of moves
    for sock, num_socks in socks_count.items():
        count += num_socks // 2
    print(count)

if __name__ == "__main__":
    main()
