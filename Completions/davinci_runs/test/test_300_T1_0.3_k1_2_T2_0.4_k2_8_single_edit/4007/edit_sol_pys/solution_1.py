

def main():
    n = int(input())
    f = list(map(int, input().split())) # f is the list of file names

    # find all the zeros (file names that are not yet assigned)
    zeros = [] # zeros is the list of indices of the unassigned file names
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)

    # assign the first non-zero to the first zero (the first unassigned file name)
    f[zeros[0]] = f.index(1) + 1

    # assign the remaining zeros to the remaining non-zeros
    for i in range(1, len(zeros)): # for each unassigned file name
        f[zeros[i]] = f[zeros[i-1]] + 1

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
