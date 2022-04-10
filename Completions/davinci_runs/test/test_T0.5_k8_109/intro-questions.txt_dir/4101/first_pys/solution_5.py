

def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    r = [0] * n
    c = [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                if i % 2 == 0:
                    r[i] = 1 - r[i]
                if j % 2 == 0:
                    c[j] = 1 - c[j]
            else:
                if i % 2 == 1:
                    r[i] = 1 - r[i]
                if j % 2 == 1:
                    c[j] = 1 - c[j]

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                if (i % 2 == 0 and r[i] == 0) or (i % 2 == 1 and r[i] == 1):
                    if (j % 2 == 0 and c[j] == 0) or (j % 2 == 1 and c[j] == 1):
                        print('NO')
                        return
            else:
                if (i % 2 == 0 and r[i] == 1) or (i % 2 == 1 and r[i] == 0):
                    if (j % 2 == 0 and c[j] == 1) or (j % 2 == 1 and c[j] == 0):
                        print('NO')
                        return

    print('YES')
    print(''.join(map(str, r)))
    print(''.join(map(str, c)))

if __name__ == '__main__':
    main()