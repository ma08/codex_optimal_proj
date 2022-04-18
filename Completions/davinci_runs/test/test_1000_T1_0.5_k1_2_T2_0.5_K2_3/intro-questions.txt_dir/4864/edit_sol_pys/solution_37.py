

r, c, zr, zc = map(int, input().split()) # input

for i in range(r): # for each row of the line
    line = input() # input line
    for j in range(zr): # for each row of the character
        for k in range(c): # for each character of the line
            for l in range(zc): # print the character
                print(line[k], end='') # print the character
        print()
