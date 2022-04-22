

t = int(input())

for i in range(t):
    n, m = [int(x) for x in input().split()]
    
    tiles = []
    
    for j in range(n):
        tiles.append([int(x) for x in input().split()])
        
    for j in range(n):
        tiles.append([int(x) for x in input().split()])
    
    tiles.sort()
    
    for j in range(n):
        for k in range(m):
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0] and tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                print("YES")
                break
            else:
                print("NO")
                break
    else:
        print("NO")
