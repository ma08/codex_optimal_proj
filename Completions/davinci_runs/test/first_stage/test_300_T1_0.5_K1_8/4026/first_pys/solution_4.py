

# SOLUTION
# The solution is to check that the sum of the elements in each row and column is the same and that the sum of the elements along the diagonal is the same.
# The sum of the elements in each row and column is the same because of the symmetric property.
# The sum of the elements along the diagonal is the same because the first element of each row and column is the same.

def can_construct(tiles, m):
    n = len(tiles)
    sum_diagonal = 0
    for i in range(n):
        sum_diagonal += tiles[i][0]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if tiles[i][0] + tiles[i][1] != tiles[j][0] + tiles[j][1] or tiles[i][0] + tiles[j][1] != sum_diagonal:
                return False
    return True

def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        tiles = []
        for j in range(n):
            row1 = list(map(int, input().split()))
            row2 = list(map(int, input().split()))
            tiles.append([row1[0], row1[1], row2[0], row2[1]])
        if can_construct(tiles, m):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()