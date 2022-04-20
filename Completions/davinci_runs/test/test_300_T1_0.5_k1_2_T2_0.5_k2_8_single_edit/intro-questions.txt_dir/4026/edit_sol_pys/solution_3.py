

t = int(input()) # number of test cases

for i in range(t):
    n, m = [int(x) for x in input().split()] # nxn board, m number of tiles
    
    tiles = [] # list of tiles
    
    for j in range(n): # input tiles
        tiles.append([int(x) for x in input().split()])
        
    for j in range(n): # input tiles
        tiles.append([int(x) for x in input().split()])
    
    tiles.sort() # sort tiles by left side
    
    for j in range(n): # swap tiles if they match
        for k in range(n): # swap tiles if they match
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0]:
                tiles[j][0], tiles[k][0] = tiles[k][0], tiles[j][0]
                tiles[j][2], tiles[k][2] = tiles[k][2], tiles[j][2]
            if tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                tiles[j][1], tiles[k][1] = tiles[k][1], tiles[j][1]
                tiles[j][3], tiles[k][3] = tiles[k][3], tiles[j][3]

    if m % 2 == 0: # even number of tiles
        if m == 2: # 2 tiles
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else: # more than 2 tiles
            print("YES")
    else: # odd number of tiles
        if m == 1: # 1 tile
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else: # more than 1 tile
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
