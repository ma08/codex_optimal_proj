

def main():
    n = int(input())
    f = list(map(int, input().split()))

    # find all the zeros and non-zeros
    zeros = []
    for i in range(n):
        if f[i] == 0:
    non_zeros = []
            zeros.append(i+1)
        if f[i] != 0:
            non_zeros.append(i+1)

    # assign the remaining zeros to the remaining non-zeros
    for i in range(len(zeros)):
        f[zeros[i]-1] = non_zeros[i]

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
