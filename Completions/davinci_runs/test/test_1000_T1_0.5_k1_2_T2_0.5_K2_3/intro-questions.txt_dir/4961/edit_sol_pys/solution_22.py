

r,s = map(int,input().split())

matrix = []

for i in range(r):
    matrix.append(list(input()))

count = 0


for i in range(r):
    for j in range(s):
        if matrix[i][j] == 'o':
            for k in range(i-1,-1,-1):
                if matrix[k][j] == 'o':
                    break
                if matrix[k][j] == '.':
                    count += 1
                    break
            for k in range(i+1,r):
                if matrix[k][j] == 'o':
                    break
                if matrix[k][j] == '.':
                    count += 1
                    break
            for k in range(j-1,-1,-1):
                if matrix[i][k] == 'o':
                    break
                if matrix[i][k] == '.':
                    count += 1
                    break
            for k in range(j+1,s):
                if matrix[i][k] == 'o':
                    break
                if matrix[i][k] == '.':
                    count += 1
                    break

print(count)
