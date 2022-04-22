

t = int(input())

def check_same(tiles):
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i][0] == tiles[j][2] and tiles[i][2] == tiles[j][0]:
                tiles[i][0], tiles[j][0] = tiles[j][0], tiles[i][0]
                tiles[i][2], tiles[j][2] = tiles[j][2], tiles[i][2]
            if tiles[i][1] == tiles[j][3] and tiles[i][3] == tiles[j][1]:
                tiles[i][1], tiles[j][1] = tiles[j][1], tiles[i][1]
                tiles[i][3], tiles[j][3] = tiles[j][3], tiles[i][3]
        
        if tiles[0][0] == tiles[i][0] and tiles[0][1] == tiles[i][1] and tiles[0][2] == tiles[i][2] and tiles[0][3] == tiles[i][3]:
            return True
        else:
            return False


def main():
    for i in range(t):
        n, m = [int(x) for x in input().split()]
        
        tiles = []
        for j in range(n):
            tiles.append([int(x) for x in input().split()])
            
        for j in range(n):
            tiles.append([int(x) for x in input().split()])
        
        tiles.sort()
        check_same(tiles)
        if m % 2 == 0:
            if m == 2:
                if check_same(tiles):
                    print("YES")
                else:
                    print("NO")
            else:
                print("YES")
        else:
            if m == 1:
                if check_same(tiles):
                    print("YES")
                else:
                    print("NO")
            else:
                if check_same(tiles):
                    print("YES")
                else:
                    print("NO")

if __name__ == "__main__":
    main()
