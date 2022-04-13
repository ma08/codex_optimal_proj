

def main():
    M, N, C = input().split()  # M = rows, N = columns, C = color
    M = int(M)
    N = int(N)
    first = []  # list of lists of the first picture
    second = []  # list of lists of the second picture
    for i in range(M):
        first.append(list(input()))
    for i in range(M):
        second.append(list(input()))
    for i in range(M):
        for j in range(N):
            if first[i][j] != C:
                first[i][j] = '.'  # if not C, then replace with '.'
            else:
                first[i][j] = 'X'  # if C, then replace with 'X'
            if second[i][j] != C:
                second[i][j] = '.'  # if not C, then replace with '.'
            else:
                second[i][j] = 'X'  # if C, then replace with 'X'
    for i in range(M):
        for j in range(N):
            if second[i][j] == 'X' and first[i][j] != 'X':
                second[i][j] = '^'  # if C in second picture and not in first, then replace with '^'
    for i in range(M):
        for j in range(N):
            if second[i][j] == '^':
                second[i][j] = '.'  # if '^', then replace with '.'
            if second[i][j] == 'X':
                second[i][j] = C  # if 'X', then replace with C
    for i in range(M):
        print(''.join(second[i]))
    print()


if __name__ == '__main__':
    main()
