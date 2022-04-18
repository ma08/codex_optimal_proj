

import sys

def main():
    n = int(sys.stdin.readline())
    socks = list(map(int, sys.stdin.readline().strip().split()))

    count = 0
    # Sort socks by type
    socks.sort()
    # Count number of socks of each type
    socks_count = dict()
    for sock in socks:
        if sock in socks_count:
            socks_count[sock] += 1
        else:
            socks_count[sock] = 1
    # Count number of moves
    for sock, num_socks in socks_count.items():
        count += num_socks // 2
    print(count)

if __name__ == "__main__":
    main()
