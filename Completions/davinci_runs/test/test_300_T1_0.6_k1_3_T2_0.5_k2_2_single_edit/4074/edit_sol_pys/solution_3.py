
import sys

sys.setrecursionlimit(10**6)

def main():
    N, K = map(int, sys.stdin.readline().strip().split())

    if N == 1:
        print(1)
        return

    min_packets = N
    for k in range(1, K + 1):
        if N % k == 0:
            packets = N // k
            if packets < min_packets:
                min_packets = packets

    print(min_packets)

if __name__ == "__main__":
    main()
