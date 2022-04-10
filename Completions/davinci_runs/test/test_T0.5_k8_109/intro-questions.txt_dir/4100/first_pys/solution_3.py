

import sys

def main():
    N, K, Q = map(int, sys.stdin.readline().split())
    players = [K] * N
    for i in range(Q):
        A = int(sys.stdin.readline())
        for j in range(N):
            if j != A-1:
                players[j] -= 1
    for i in range(N):
        if players[i] > 0:
            print("Yes")
        else:
            print("No")
    return

if __name__ == "__main__":
    main()