

t = int(input())

for i in range(t):
    n, m = [int(x) for x in input().split()] # get input
    tiles = []

    for j in range(n):
        tiles.append([int(x) for x in input().split()]) # get input

    for j in range(n):
        tiles.append([int(x) for x in input().split()]) # get input

    tiles.sort() # sort the list

    for j in range(n): # loop through the list
        for k in range(n): # loop through the list
            # swap the values if they are equal
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0]:
                tiles[j][0], tiles[k][0] = tiles[k][0], tiles[j][0]
                tiles[j][2], tiles[k][2] = tiles[k][2], tiles[j][2]
            if tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                tiles[j][1], tiles[k][1] = tiles[k][1], tiles[j][1]
                tiles[j][3], tiles[k][3] = tiles[k][3], tiles[j][3]

    if m % 2 == 0: # if m is even
        if m == 2: # if m is equal to 2
            # check if the tiles are equal
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0] and tiles[1][0] == tiles[1][1] and tiles[1][1] == tiles[1][2] and tiles[1][2] == tiles[1][3] and tiles[1][3] == tiles[1][0]:
                print("YES") # print yes
            else:
                print("NO") # print no
        else: # if m is not equal to 2
            print("YES") # print yes
    else: # if m is odd
        if m == 1: # if m is equal to 1
            # check if the tiles are equal
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0] and tiles[1][0] == tiles[1][1] and tiles[1][1] == tiles[1][2] and tiles[1][2] == tiles[1][3] and tiles[1][3] == tiles[1][0]:
                print("YES") # print yes
            else:
                print("NO") # print no
        else: # if m is not equal to 1
            # check if the tiles are equal
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0] and tiles[1][0] == tiles[1][1] and tiles[1][1] == tiles[1][2] and tiles[1][2] == tiles[1][3] and tiles[1][3] == tiles[1][0]:
                print("YES") # print yes
            else:
                print("NO") # print no
