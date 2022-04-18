

r, c, zr, zc = map(int, input().split()) # input line

for i in range(r):
    line = input()
    for j in range(zr):
        for k in range(c):
            for l in range(zc):
                print(line[k], end='') # print the character
        print() # for each row of the character
