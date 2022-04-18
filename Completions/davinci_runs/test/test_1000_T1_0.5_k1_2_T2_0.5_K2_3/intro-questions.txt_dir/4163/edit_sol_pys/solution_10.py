

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    D = []
    for i in range(N):
        D.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(N-1):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1]:
            if i < N-2:
                if D[i+2][0] == D[i+2][1]:
                    print("Yes")
                    return
                else:
                    print("No")
                    return
            else:
                print("No")
                return
    print("No")
    return

if __name__ == "__main__":
    main()
