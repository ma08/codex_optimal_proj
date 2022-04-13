
r, c, zr, zc = map(int, input().split()) # dimensions of the input matrix, and zoom factors

for i in range(r):
    line = input() # read a line of input
    for j in range(zr): # zoom row factor
        for k in range(c): # column
            for l in range(zc): # zoom column factor
                print(line[k], end='') # print a character of the line
        print() # print a newline
