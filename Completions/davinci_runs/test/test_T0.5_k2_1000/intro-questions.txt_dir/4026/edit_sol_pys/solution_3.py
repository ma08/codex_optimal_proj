

t = int(input())

for i in range(t):
    n, m = [int(x) for x in input().split()]
    
    tiles = [[] for x in range(n)]
    
    for j in range(n):
        tiles[j] = [int(x) for x in input().split()]
        
    for j in range(n):
        tiles[j] += [int(x) for x in input().split()]
    
    tiles.sort(key=lambda x: x[0])
    
    for j in range(n):
        for k in range(n):
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0] and tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                tiles[j], tiles[k] = tiles[k], tiles[j]

    if m == 1:
        if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
            print("NO")
    elif m == 2:
        if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
            print("YES")
        else:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
