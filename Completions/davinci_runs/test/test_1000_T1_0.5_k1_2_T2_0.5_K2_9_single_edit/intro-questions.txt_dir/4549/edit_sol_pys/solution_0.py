

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                if i == h - 1 and j == w - 1:
                    continue
                elif i == h - 1 and j == w - 2 and s[i][j + 1] == '#':
                    continue
                elif i == h - 2 and j == w - 1 and s[i + 1][j] == '#':
                    continue
                elif i == h - 1 or j == w - 1:
                    print('No')
                    return
                elif s[i + 1][j] == '.' and s[i][j + 1] == '.':
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()
