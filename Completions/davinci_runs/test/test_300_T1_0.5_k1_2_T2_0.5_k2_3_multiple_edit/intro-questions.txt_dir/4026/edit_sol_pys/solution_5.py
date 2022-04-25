n, m = [int(x) for x in input().split()]
tiles = []
for i in range(n):
    tiles.append([int(x) for x in input().split()])
for i in range(n):
    tiles.append([int(x) for x in input().split()])
for i in range(n):
    tiles[i].sort()
tiles.sort(key=lambda x: (x[0], x[1]))
if m % 2 == 0:
    if m == 2:
        if tiles[0][0] == tiles[1][0] and tiles[0][1] == tiles[1][1] and tiles[0][2] == tiles[1][2] and tiles[0][3] == tiles[1][3]:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    if m == 1:
        if tiles[0][0] == tiles[1][0] and tiles[0][1] == tiles[1][1] and tiles[0][2] == tiles[1][2] and tiles[0][3] == tiles[1][3]:
            print("YES")
        else:
            print("NO")
    else:
        if tiles[0][0] == tiles[1][0] and tiles[0][1] == tiles[1][1] and tiles[0][2] == tiles[1][2] and tiles[0][3] == tiles[1][3]:
            print("YES")
        else:
            print("NO")
