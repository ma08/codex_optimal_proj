

def get_input():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        tiles = []
        for j in range(n):
            t1 = list(map(int, input().split()))
            t2 = list(map(int, input().split()))
            tiles.append([t1, t2])
        yield n, m, tiles

def is_symmetric(n, m, tiles):
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if not any([t[0][0] == tiles[i][j] and t[1][0] == tiles[j][i] for t in tiles]):
                return False
    return True

if __name__ == '__main__':
    for n, m, tiles in get_input():
        print('YES' if is_symmetric(n, m, tiles) else 'NO')