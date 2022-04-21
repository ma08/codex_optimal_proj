import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    D = []
    for i in range(N):
        D.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # 横
    for i in range(N):
        for j in range(N-2):
            if D[i][j] == D[i][j+1] and D[i][j+1] == D[i][j+2]:
                print("Yes")
                return
    # 縦
    for j in range(N):
        for i in range(N-2):
            if D[i][j] == D[i+1][j] and D[i+1][j] == D[i+2][j]:
                print("Yes")
                return
    # 斜め
    for i in range(N-2):
        for j in range(N-2):
            if D[i][j] == D[i+1][j+1] and D[i+1][j+1] == D[i+2][j+2]:
                print("Yes")
                return
    for i in range(N-2):
        for j in range(N-2):
            if D[i][j+2] == D[i+1][j+1] and D[i+1][j+1] == D[i+2][j]:
                print("Yes")
                return
    print("No") 
    return

if __name__ == "__main__":
    main()
