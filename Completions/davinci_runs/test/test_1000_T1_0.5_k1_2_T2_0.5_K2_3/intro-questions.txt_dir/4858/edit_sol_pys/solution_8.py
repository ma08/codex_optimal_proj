

def main():
    M, N, C = input().split()
    M = int(M)
    N = int(N)
    first = []
    second = []
    for _ in range(M):
        first.append(list(input()))
    for _ in range(M):
        second.append(list(input()))
    for i in range(M):
        for j in range(N):
            if first[i][j] != C:
                first[i][j] = '.'
            else:
                first[i][j] = 'x'
            if second[i][j] != C:
                second[i][j] = '.'
            else:
                second[i][j] = 'x'
    for i in range(M):
        for j in range(N):
            if second[i][j] == 'x' and first[i][j] != 'x':
                second[i][j] = '^'
    for i in range(M):
        for j in range(N):
            if second[i][j] == '^':
                second[i][j] = '.'
            if second[i][j] == 'x':
                second[i][j] = C
    for i in range(M):
        print(''.join(second[i]))
    print()

if __name__ == '__main__':
    main()
