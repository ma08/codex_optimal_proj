

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    S = [[0,0] for i in range(N)]
    for i in range(N):
        S[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(N-2):
        if S[i][0] == S[i][1] and S[i+1][0] == S[i+1][1] and S[i+2][0] == S[i+2][1]:
            print("Yes")
            return
    print("No")
    return

if __name__ == "__main__":
    main()
