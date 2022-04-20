

def main():
    n, m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    r = ''
    c = ''
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                r += '0'
                c += '0'
            else:
                if i % 2 == 0:
                    r += '1'
                    c += '0'
                else:
                    r += '0'
                    c += '1'
    print('YES')
    print(r)
    print(c)

if __name__ == "__main__":
    main()