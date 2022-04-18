

def main():
    n, m = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(n)]
    t = [list(map(int, input().split())) for _ in range(m)]

    for i in range(n):
        for j in range(n):
            if s[i][j] == t[i][j]:
                continue
            for k in range(n):
                s[i][k] ^= 1
            for k in range(n):
                s[k][j] ^= 1

    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()
