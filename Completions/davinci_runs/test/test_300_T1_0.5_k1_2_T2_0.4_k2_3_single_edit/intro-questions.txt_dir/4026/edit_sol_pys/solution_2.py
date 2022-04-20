

t = int(input())  # number of test cases

for i in range(t):
    n, m = [int(x) for x in input().split()]  # number of tiles, number of rows
    
    tiles = []  # list of tiles
    
    for j in range(n):
        tiles.append([int(x) for x in input().split()])  # input of tiles
        
    for j in range(n):
        tiles.append([int(x) for x in input().split()])  # input of tiles
    
    tiles.sort()  # sort the tiles
    
    for j in range(n):
            # swap the tiles
        for k in range(n):
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0]:
                tiles[j][0], tiles[k][0] = tiles[k][0], tiles[j][0]
                tiles[j][2], tiles[k][2] = tiles[k][2], tiles[j][2]
            if tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                tiles[j][1], tiles[k][1] = tiles[k][1], tiles[j][1]
                tiles[j][3], tiles[k][3] = tiles[k][3], tiles[j][3]
        # check if the first tile is the same as the last tile

    if m % 2 == 0:
        if m == 2:
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else:
        # check if the first tile is the same as the last tile
            print("YES")
    else:
        if m == 1:
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else:
            # check if the first tile is the same as the last tile
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
