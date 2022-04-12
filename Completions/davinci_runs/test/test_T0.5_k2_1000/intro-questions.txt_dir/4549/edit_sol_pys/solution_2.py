
def main():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())

        for j in range(w):            
            if s[i][j] == '#' and s[i-1][j] == '.' and s[i+1][j] == '.' and s[i][j-1] == '.' and s[i][j+1] == '.':
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()
