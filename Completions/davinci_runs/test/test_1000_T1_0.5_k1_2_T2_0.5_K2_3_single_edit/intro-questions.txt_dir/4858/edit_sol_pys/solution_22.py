

def main():
    M, N, C = input().split()   #input M, N and C
    M = int(M)
    N = int(N)
    first = []     #first is the first image
    second = []    #second is the second image
    #inputs the first image
    for i in range(M):
    #inputs the second image
        first.append(list(input()))
    for i in range(M):
    #replaces the C with X or .
        second.append(list(input()))
    for i in range(M):
        for j in range(N):
            if first[i][j] != C:
                first[i][j] = '.'
            else:
                first[i][j] = 'X'
            if second[i][j] != C:
                second[i][j] = '.'
            else:
                second[i][j] = 'X'
    #replaces the X with ^
    for i in range(M):
        for j in range(N):
            if second[i][j] == 'X' and first[i][j] != 'X':
                second[i][j] = '^'
    #replaces the ^ with . and the X with C
    for i in range(M):
        for j in range(N):
            if second[i][j] == '^':
                second[i][j] = '.'
            if second[i][j] == 'X':
                second[i][j] = C
    #prints the second image
    for i in range(M):
        print(''.join(second[i]))
    print()

if __name__ == '__main__':
    main()
