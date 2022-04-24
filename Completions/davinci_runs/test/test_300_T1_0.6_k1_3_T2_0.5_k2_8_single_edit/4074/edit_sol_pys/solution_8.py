

import sys

sys.setrecursionlimit(10**6)

def get_min_packets(shovels, types, memo):
    if shovels == 0: return 0
    if shovels < 0: return sys.maxsize
    if memo[shovels] != -1: return memo[shovels]
    min_packets = sys.maxsize - 1
    for t in range(1, types + 1):
        packets = get_min_packets(shovels - t, types, memo)
        if min_packets > packets:
            min_packets = packets
    memo[shovels] = min_packets + 1
    return memo[shovels]

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        memo = [-1] * (N + 1)
        print(get_min_packets(N, K, memo))

if __name__ == "__main__":
    main()
