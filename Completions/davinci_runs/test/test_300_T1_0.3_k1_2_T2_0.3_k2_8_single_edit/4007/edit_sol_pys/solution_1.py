

def main():
    n = int(input())
    f = list(map(int, input().split()))  # f is a list of integers

    # find all the zeros in f
    zeros = []
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)

    # find the first non-zero in f
    non_zero = -1
    for i in range(n):
        if f[i] != 0:
            non_zero = i
            break

    # find the first zero in f
    zero = -1
    for i in range(n):
        if f[i] == 0:
            zero = i
            break

    # assign the first non-zero in f to the first zero in f
    f[zero] = non_zero + 1

        # assign the remaining zeros in f to the remaining non-zeros in f
    for i in range(1, len(zeros)):
        f[zeros[i]] = f[zeros[i-1]] + 1

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
