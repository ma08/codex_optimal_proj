

import sys

input = sys.stdin.readline

def main():
    h, w, k = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]

    ans = 0
    for i in range(2 ** h):
        for j in range(2 ** w):
            cnt = 0
            for x in range(h):
                if (i >> x) & 1:
                    continue
                for y in range(w):
                    if (j >> y) & 1:
                        continue
                    if grid[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()