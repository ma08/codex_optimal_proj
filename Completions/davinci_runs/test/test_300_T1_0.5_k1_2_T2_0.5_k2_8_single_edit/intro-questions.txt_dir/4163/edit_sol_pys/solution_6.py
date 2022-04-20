
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    D = [0]*N
    for i in range(N):
        D[i] = [0]*2
    for i in range(N):
        D.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1] and D[i+3][0] == D[i+3][1]:
            print("Yes")
            return
    print("No")
    return

if __name__ == "__main__":
    main()
