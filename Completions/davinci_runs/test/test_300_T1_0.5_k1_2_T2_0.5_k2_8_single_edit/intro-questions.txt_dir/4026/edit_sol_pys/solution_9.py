

n, m = [int(x) for x in input().split()]
    
tiles = []
    
for i in range(n):
    tiles.append([int(x) for x in input().split()])
        
for i in range(n):
    tiles.append([int(x) for x in input().split()])
    
tiles.sort()

for i in range(n):
    for j in range(n):
        if tiles[i][0] == tiles[j][2] and tiles[i][2] == tiles[j][0]:
            tiles[i][0], tiles[j][0] = tiles[j][0], tiles[i][0]
            tiles[i][2], tiles[j][2] = tiles[j][2], tiles[i][2]
        if tiles[i][1] == tiles[j][3] and tiles[i][3] == tiles[j][1]:
            tiles[i][1], tiles[j][1] = tiles[j][1], tiles[i][1]
            tiles[i][3], tiles[j][3] = tiles[j][3], tiles[i][3]

if m % 2 == 0:
    if m == 2:
        if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
        print("NO")
        else:
            print("YES")
    else:
    if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
        print("YES")
    else:
        print("NO")
else:
    if m == 1:
    if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
        print("YES")
    else:
        print("NO")
else:
    if tiles[0][0] == tiles[0][1] and tiles[0][1] == tiles[0][2] and tiles[0][2] == tiles[0][3] and tiles[0][3] == tiles[0][0]:
        print("YES")
    else:
        print("NO")
