
#-----main-----
#read input
H, W, K = map(int, input().split()) #H:高さ, W:幅, K:黒マスの数
c = [list(input()) for i in range(H)] #c[i][j]:i行j列のマスの状態

#initialize variables
ans = 0

#loop for all cases
for i in range(1, 2**H):
    #get row index (行のインデックスを取得)
    row = []
    for j in range(H):
        if (i>>j) & 1:
            row.append(j)
    for j in range(1, 2**W):
        #get column index (列のインデックスを取得)
        column = []
        for k in range(W):
            if (j>>k) & 1:
                column.append(k)
        #count black squares (黒マスの数を数える)
        tmp = 0
        for k in row:
            for l in column:
                if c[k][l] == '#':
                    tmp += 1
        if tmp == K:
            ans += 1

print(ans)
