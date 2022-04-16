

def main():
    n, m = map(int, input().split())
    a = [input() for i in range(n)]
    b = [input() for i in range(m)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if a[i][j:j+m] == b[0]:
                for k in range(1, m):
                    if a[i+k][j:j+m] != b[k]:
                        break
                else:
                    print('Yes')
                    exit()
    print('No')


if __name__ == '__main__':
    main()
