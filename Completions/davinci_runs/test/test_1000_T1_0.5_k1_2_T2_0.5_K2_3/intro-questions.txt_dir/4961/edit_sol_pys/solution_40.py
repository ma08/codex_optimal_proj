
r,s = map(int,input().split()) # input number of rows and columns

matrix = [] # create matrix

for i in range(r): # input matrix
    matrix.append(list(input())) # add matrix row by row

count = 0 # set count to 0

for i in range(r): # iterate through rows
    for j in range(s): # iterate through columns
        if matrix[i][j] == 'o': # check if current cell is o
            if i != 0 and matrix[i-1][j] == 'o': # check if cell above is o
                count += 1 # increment count by 1
            if i != r-1 and matrix[i+1][j] == 'o': # check if cell below is o
                count += 1 # increment count by 1
            if j != 0 and matrix[i][j-1] == 'o': # check if cell to the left is o
                count += 1 # increment count by 1
            if j != s-1 and matrix[i][j+1] == 'o': # check if cell to the right is o
                count += 1 # increment count by 1

print(count) # print count
