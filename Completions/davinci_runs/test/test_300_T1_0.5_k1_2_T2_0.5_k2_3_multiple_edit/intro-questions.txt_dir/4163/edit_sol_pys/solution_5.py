

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    D = []
    for i in range(N):
        D.append(list(map(int, sys.stdin.readline().rstrip().split())))  # リストに入れる
    for i in range(N):
        if D[i][0] == D[i][1]:
            for j in range(i+1, N):
                if D[j][0] == D[j][1]:
                    for k in range(j+1, N):
                        if D[k][0] == D[k][1]:
                            print("Yes")
                            return
    print("No") 
    return

if __name__ == "__main__":
    main()
