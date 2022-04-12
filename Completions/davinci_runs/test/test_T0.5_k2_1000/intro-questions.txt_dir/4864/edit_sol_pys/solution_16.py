
r, c, zr, zc = map(int, input().split()) #r = rows, c = columns, zr = row zoom, zc = column zoom

for i in range(r):
    line = input() #input a line
    #print the line zr times
    for j in range(zr):
        #print each character in the line zc times
        for k in range(c):
            for l in range(zc):
                print(line[k], end='')
        print()
