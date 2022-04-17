

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    D = []
    D = []
    for i in range(N):
    for i in range(N):
        D.append(list(map(int, sys.stdin.readline().rstrip().split())))
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]: print("Yes")
        else: print("No")
    return

if __name__ == "__main__":
    main()
