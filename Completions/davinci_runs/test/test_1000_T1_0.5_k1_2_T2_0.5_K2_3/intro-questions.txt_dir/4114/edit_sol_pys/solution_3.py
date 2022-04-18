import sys
N = int(input())

X_Y_H = []
for i in range(N):
    X_Y_H.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(i+1, N):
        if X_Y_H[i][0] == X_Y_H[j][0]:
            if X_Y_H[i][1] == X_Y_H[j][1]:
                if X_Y_H[i][2] != X_Y_H[j][2]:
                    print("No")
                    exit()
            else:
                C_X = X_Y_H[i][0]
                C_Y = (X_Y_H[i][1] + X_Y_H[j][1]) / 2
                if X_Y_H[i][2] == X_Y_H[j][2]:
                    H = abs(X_Y_H[i][1] - X_Y_H[j][1]) + X_Y_H[i][2]
                else:
                    H = abs(X_Y_H[i][1] - X_Y_H[j][1]) + max(X_Y_H[i][2], X_Y_H[j][2])
                break
for i in range(N):
    if X_Y_H[i][0] == C_X and X_Y_H[i][1] == C_Y:
        if X_Y_H[i][2] != H:
            print("No")
            exit()
    else:
        if X_Y_H[i][2] != abs(C_X - X_Y_H[i][0]) + abs(C_Y - X_Y_H[i][1]) + H:
            print("No")
            exit()
print(C_X, C_Y, H)
