

def main():
    H, W = [int(x) for x in input().split()]
    s = [input() for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if s[i][j] == '#':
                if i == H - 1 and j == W - 1:
                    continue
                elif i == H - 1 and j == W - 2 and s[i][j + 1] == '#':
                    continue
                elif i == H - 2 and j == W - 1 and s[i + 1][j] == '#':
                    continue
                elif i == H - 1 or j == W - 1:
                    print('No')
                    return
                elif s[i + 1][j] == '.' and s[i][j + 1] == '.':
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()
