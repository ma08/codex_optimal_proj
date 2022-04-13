
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    S = []
    for i in range(N):
        S.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(N):
        for j in range(N):
            if S[i][j] == 1:
                print(i+1, j+1)
                return
    return

if __name__ == "__main__":
    main()
