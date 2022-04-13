

r, c, zr, zc = map(int, raw_input().split())

    # input line
for i in range(r):
    # for each row of the line
    line = raw_input()
        # for each character of the line
    for j in range(zr):
            # for each row of the character
        for k in range(c):
                # print the character
            for l in range(zc):
                print(line[k], end='')
        print()
