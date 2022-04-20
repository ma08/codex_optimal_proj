
import math
import sys

sys.setrecursionlimit(10**6)

def get_min_packets(shovels, types, packets):
    if shovels == 0 or shovels == 1:
        return shovels

    if packets[shovels] != -1:
        return packets[shovels]

    min_packets = sys.maxsize - 1
    for t in range(1, types + 1):
        packets_required = get_min_packets(shovels - t, types, packets)
        if packets_required < min_packets:
            min_packets = packets_required
    packets[shovels] = min_packets + 1
    return packets[shovels]

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        packets = [-1] * (N + 1)
        print(get_min_packets(N, K, packets))

if __name__ == "__main__":
    main()
