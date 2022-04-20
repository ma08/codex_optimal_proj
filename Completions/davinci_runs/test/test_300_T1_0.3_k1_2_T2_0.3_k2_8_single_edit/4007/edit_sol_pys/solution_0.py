

def main():
    n = int(input())
    f = list(map(int, input().split()))

    # find the first non-zero
    non_zero = 0
    for i in range(n):
        if f[i] != 0:
            non_zero = i
            break

    # find the first zero
    zero = 0
    for i in range(n):
        if f[i] == 0:
            zero = i
            break

    # assign the first non-zero to the first zero
    f[zero] = non_zero + 1

    # assign the remaining zeros to the remaining non-zeros
    for i in range(zero+1, n):
        if f[i] == 0:
            f[i] = f[i-1] + 1

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
