import sys

def main():
    H, W, K = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(2**H):
        for j in range(2**W):
            num = 0
            for x in range(H):
                for y in range(W):
                    if ((i >> x) & 1) == 0 and ((j >> y) & 1) == 0 and c[x][y] == '#':
                        num += 1
            if num == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
