

r,s = map(int,input().split())

matrix = []

for i in range(r):
    matrix.append(list(input()))

count = 0

for i in range(r):
    for j in range(s):
        if matrix[i][j] == 'x':
            if i != 0 and matrix[i-1][j] == 'x':
                count += 1
            if i != r-1 and matrix[i+1][j] == 'x':
                count += 1
            if j != 0 and matrix[i][j-1] == 'x':
                count += 1
            if j != s-1 and matrix[i][j+1] == 'x':
                count += 1

print(count)
