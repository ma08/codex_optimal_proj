

def main():
    h, w = map(int, input().split())  # read a list of integers, 2 in this case
    s = [input() for _ in range(h)]

    for i in range(h):  # loop over the rows
        for j in range(w):  # loop over the columns
            if s[i][j] == '#':
                if i == 0 and j == 0:
                    if s[i+1][j] == '.' and s[i][j+1] == '.':
                        print('No')
                        exit()
                elif i == 0 and j == w-1:
                    if s[i+1][j] == '.' and s[i][j-1] == '.':
                        print('No')
                        exit()
                elif i == h-1 and j == 0:
                    if s[i-1][j] == '.' and s[i][j+1] == '.':
                        print('No')
                        exit()
                elif i == h-1 and j == w-1:
                    if s[i-1][j] == '.' and s[i][j-1] == '.':
                        print('No')
                        exit()
                elif i == 0:
                    if s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                        print('No')
                        exit()
                elif i == h-1:
                    if s[i-1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                        print('No')
                        exit()
                elif j == 0:
                    if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j+1] == '.':
                        print('No')
                        exit()
                elif j == w-1:
                    if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.':
                        print('No')
                        exit()
                else:
                    if s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                        print('No')
                        exit()
    print('Yes')

if __name__ == '__main__':
    main()
