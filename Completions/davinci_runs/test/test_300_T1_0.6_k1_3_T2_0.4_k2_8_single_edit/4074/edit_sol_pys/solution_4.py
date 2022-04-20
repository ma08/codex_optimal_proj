
import sys
sys.setrecursionlimit(10**6)

def get_min_packets(shovels, types):
    if shovels < 0:
        return None
    if shovels == 0:
        return 0
    if shovels == 1:
        return 1

    min_packets = sys.maxsize
    for t in range(types, 0, -1):
        packets = get_min_packets(shovels - t, types)
        if packets is not None and packets < min_packets:
            min_packets = packets
    if min_packets == sys.maxsize:
        return None
    return min_packets + 1
def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        print(get_min_packets(N, K))
if __name__ == "__main__":
    main()
