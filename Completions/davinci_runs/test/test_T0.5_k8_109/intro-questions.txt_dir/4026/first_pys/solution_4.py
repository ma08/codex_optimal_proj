

import sys

def main():
    n = int(input())
    for _ in range(n):
        n, m = map(int, input().split())
        tiles = [None] * n
        for i in range(n):
            tiles[i] = [[0] * 2 for _ in range(2)]
            tiles[i][0][0], tiles[i][0][1] = map(int, input().split())
            tiles[i][1][0], tiles[i][1][1] = map(int, input().split())
        if m % 2 == 1:
            print('NO')
            continue
        ans = False
        for i in range(n):
            for j in range(n):
                if tiles[i][0][0] == tiles[j][1][1] and tiles[i][0][1] == tiles[j][1][0] and tiles[i][1][0] == tiles[j][0][1] and tiles[i][1][1] == tiles[j][0][0]:
                    ans = True
                    break
        if ans:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()