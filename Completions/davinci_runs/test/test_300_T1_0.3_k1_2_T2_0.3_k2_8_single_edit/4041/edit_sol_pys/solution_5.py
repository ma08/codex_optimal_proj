
def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if a[i][j] == b[0][0]:
                ok = True
                for k in range(m):
                    for l in range(m):
                        if a[i + k][j + l] != b[k][l]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    print('Yes')
                    exit()
    print('No')


if __name__ == '__main__':
    main()
