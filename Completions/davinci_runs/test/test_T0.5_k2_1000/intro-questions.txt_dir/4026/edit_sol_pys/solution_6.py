

t = int(input()) # number of test cases

for i in range(t):
    n, m = [int(x) for x in input().split()] # n = number of tiles, m = number of rotations
    
    tiles = [[] for x in range(n)] # list of tiles
    
    for j in range(n):
        tiles[j] = [int(x) for x in input().split()] # first half of tile
        
    for j in range(n):
        tiles[j] += [int(x) for x in input().split()] # second half of tile
    
    tiles.sort(key=lambda x: x[0]) # sort tiles by first element
    
    for j in range(n):
            # check if tiles are the same
        for k in range(n):
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0] and tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                # swap tiles
                tiles[j], tiles[k] = tiles[k], tiles[j]

            # check if all tiles are the same
    if m % 2 == 0:
        if m == 2:
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else:
            print("YES")
            # check if all tiles are the same
    else:
        if m == 1:
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else:
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                # check if all tiles are the same
                print("YES")
            else:
                print("NO")
