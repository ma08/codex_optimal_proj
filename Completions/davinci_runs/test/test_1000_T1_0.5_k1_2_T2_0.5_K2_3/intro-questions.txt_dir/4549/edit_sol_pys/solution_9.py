
def solve():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())

    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                if i == 0 and j == 0 and s[i+1][j] == '.' and s[i][j+1] == '.':
                    print('No')
                    exit()
                elif i == 0 and j == w-1 and s[i+1][j] == '.' and s[i][j-1] == '.':
                    print('No')
                    exit()
                elif i == h-1 and j == 0 and s[i-1][j] == '.' and s[i][j+1] == '.':
                    print('No')
                    exit()
                elif i == h-1 and j == w-1 and s[i-1][j] == '.' and s[i][j-1] == '.':
                    print('No')
                    exit()
                elif i == 0 and s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                    print('No')
                    exit()
                elif i == h-1 and s[i-1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                    print('No')
                    exit()
                elif j == 0 and s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j+1] == '.':
                    print('No')
                    exit()
                elif j == w-1 and s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.':
                    print('No')
                    exit()
                elif s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                    print('No')
                    exit()
    print('Yes')

if __name__ == '__main__':
    solve()
