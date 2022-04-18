

def is_same(arr):
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3] and arr[3] == arr[0]:
        return True
    else:
        return False

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
        for k in range(n):
            if tiles[j][0] == tiles[k][2] and tiles[j][2] == tiles[k][0]:
                tiles[j][0], tiles[k][0] = tiles[k][0], tiles[j][0]
                tiles[j][2], tiles[k][2] = tiles[k][2], tiles[j][2]
            if tiles[j][1] == tiles[k][3] and tiles[j][3] == tiles[k][1]:
                tiles[j][1], tiles[k][1] = tiles[k][1], tiles[j][1]
                tiles[j][3], tiles[k][3] = tiles[k][3], tiles[j][3]

    if m == 1:
        if is_same(tiles[0]):
            print("NO")
    elif m == 2:
        if is_same(tiles[0]):
            print("YES")
        else:
            print("NO")
    elif m % 2 == 0:
        if is_same(tiles[0]):
            print("YES")
        else:
            print("YES")
        if is_same(tiles[0]):
            print("YES")
        else:
            print("NO")
