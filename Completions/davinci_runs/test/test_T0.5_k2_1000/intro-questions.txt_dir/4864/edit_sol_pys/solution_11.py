#input
r, c, zr, zc = map(int, input().split()) #row, column, zoom row, zoom column

for i in range(r):
    line = input() #input each line
    for k in range(zr):
        for j in range(c):
            for l in range(zc):
                print(line[j], end='') #print each letter in the line
        print() #print new line
