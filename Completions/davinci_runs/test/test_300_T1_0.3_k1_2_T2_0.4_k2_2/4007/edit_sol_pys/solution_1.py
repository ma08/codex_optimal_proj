
def main():
    n = int(input())
    f = list(map(int, input().split()))

    # find all the zeros
    zeros = []
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)

    # find the first non-zero
    non_zero = -1
    for i in range(n):
        if f[i] != 0:
            non_zero = i
            break

    # find the first zero
    zero = -1
    for i in range(n):
        if f[i] == 0:
            zero = i
            break

    # assign the first non-zero to the first zero
    f[zero] = non_zero + 1

    # assign the remaining zeros to the remaining non-zeros
    for i in range(1, len(zeros)):
        f[zeros[i]] = f[zeros[i-1]] + 1

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
