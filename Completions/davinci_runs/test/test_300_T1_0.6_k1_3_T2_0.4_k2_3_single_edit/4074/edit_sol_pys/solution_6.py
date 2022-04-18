
import sys

sys.setrecursionlimit(10**6)


def get_min_packets(shovels, types):
    if shovels < 0:  # if shovels is negative, we can't buy any shovels
        return None
    if shovels == 0:  # if shovels is zero, we don't need to buy any shovels
        return 0
    if shovels == 1:  # if shovels is one, we have to buy a packet of one shovel
        return 1

    min_packets = sys.maxsize  # set min_packets to max value
    for t in range(types, 0, -1):  # iterate from types to 1
        packets = get_min_packets(shovels - t, types)  # get min packets for shovels - t
        if packets is not None and packets < min_packets:  # if packets is not None and less than min_packets
            min_packets = packets  # update min_packets
    if min_packets == sys.maxsize:  # if min_packets is still max value, we can't buy any shovels
        return None
    return min_packets + 1  # return min_packets + 1


def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        print(get_min_packets(N, K))


if __name__ == "__main__":
    main()
