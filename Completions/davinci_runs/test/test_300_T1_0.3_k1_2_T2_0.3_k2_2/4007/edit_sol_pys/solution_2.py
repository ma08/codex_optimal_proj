

def main():
    n = int(input())  # number of elements
    f = list(map(int, input().split()))  # list of elements

    # find all the zeros in the list
    zeros = []
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)

    # find the first non-zero in the list
    non_zero = -1
    for i in range(n):
        if f[i] != 0:
            non_zero = i
            break

    # find the first zero in the list
    zero = -1
    for i in range(n):
        if f[i] == 0:
            zero = i
            break

    # assign the first non-zero to the first zero in the list
    f[zero] = non_zero + 1

    # assign the remaining zeros to the remaining non-zeros in the list
    for i in range(1, len(zeros)):
        f[zeros[i]] = f[zeros[i-1]] + 1

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
