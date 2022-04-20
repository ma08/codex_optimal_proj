

t = int(input())  #number of test cases

for i in range(t):
    n, m = [int(x) for x in input().split()] #number of tiles and number of moves
    
    tiles = [] #list of tiles
    
    for j in range(n):
        tiles.append([int(x) for x in input().split()]) #adds tiles to the list
        
    for j in range(n): #adds tiles to the list
        tiles.append([int(x) for x in input().split()])
    
    tiles.sort() #sorts the list
    
    for j in range(n): #switches the tiles
        for k in range(n):
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0]:
                tiles[j][0], tiles[k][0] = tiles[k][0], tiles[j][0]
                tiles[j][2], tiles[k][2] = tiles[k][2], tiles[j][2]
            if tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                tiles[j][1], tiles[k][1] = tiles[k][1], tiles[j][1]
                tiles[j][3], tiles[k][3] = tiles[k][3], tiles[j][3]

    if m % 2 == 0: #if the number of moves is even
        if m == 2: #if the number of moves is 2
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else: #if the number of moves is even and not 2
            print("YES")
    else: #if the number of moves is odd
        if m == 1: #if the number of moves is 1
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
        else: #if the number of moves is odd and not 1
            if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
                print("YES")
            else:
                print("NO")
