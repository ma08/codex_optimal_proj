
import sys

sys.setrecursionlimit(10**6)


def get_min_packets(shovels, types):
    if shovels == 0:
        return 0
    if shovels < 0:
        return sys.maxsize

    min_packets = sys.maxsize
        min_packets = min(min_packets, packets + 1)
    if min_packets == sys.maxsize:
        return sys.maxsize
    return min_packets


def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        print(get_min_packets(N, K))


if __name__ == "__main__":
    main()
