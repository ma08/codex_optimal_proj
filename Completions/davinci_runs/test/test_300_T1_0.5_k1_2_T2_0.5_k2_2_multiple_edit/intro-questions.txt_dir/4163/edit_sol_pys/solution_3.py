

import sys

def main():
    N = int(sys.stdin.readline().strip())
    D = [[0 for i in range(2)] for j in range(N)]
    for i in range(N):
        D[i][0], D[i][1] = map(int, sys.stdin.readline().strip().split())
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")
    return

if __name__ == "__main__":
    main()
