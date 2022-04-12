

def main():
    m, n, c = input().split()
    m = int(m)
    n = int(n)
    first = []
    second = []
    for i in range(m):
        first.append(list(input()))
    for i in range(m):
        second.append(list(input()))
    for i in range(m):
        for j in range(n):
            if first[i][j] != c:
                first[i][j] = '.'
            else:
                first[i][j] = 'X'
            if second[i][j] != c:
                second[i][j] = '.'
            else:
                second[i][j] = 'X'
    for i in range(m):
        for j in range(n):
            if second[i][j] == 'X' and first[i][j] != 'X':
                second[i][j] = '^'
    for i in range(m):
        for j in range(n):
            if second[i][j] == '^':
                second[i][j] = '.'
            if second[i][j] == 'X':
                second[i][j] = c
    for i in range(m):
        print(''.join(second[i]))
    print()

if __name__ == '__main__':
    main()
