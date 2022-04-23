

#read input
H, W, K = map(int, input().split())
c = [list(input()) for i in range(H)]

#initialize variables
ans = 0

#loop for all cases 
for i in range(1, 2**H):
    #get row index
    row = []
    for j in range(H):
        if (i>>j) & 1:
            row.append(j)
    for j in range(1, 2**W):
        #get column index
        column = []
        for k in range(W):
            if (j>>k) & 1:
                column.append(k)
        #count black squares
        tmp = 0
        for k in row:
            for l in column:
                if c[k][l] == '#':
                    tmp += 1
        if tmp == K:
            ans += 1

print(ans)
