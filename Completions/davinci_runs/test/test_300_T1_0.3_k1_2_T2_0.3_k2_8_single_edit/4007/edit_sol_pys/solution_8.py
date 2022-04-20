

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # find the first non-zero
    non_zero = 0
    for i in range(m):
        if b[i] != 0:
            non_zero = i
            break

    zero = 0
    for i in range(m):
        if b[i] == 0:
            zero = i
            break

    # assign the first non-zero to the first zero and remove it from the list
    b[zero] = a[non_zero]
    a.pop(non_zero)

    # assign the remaining zeros to the remaining non-zeros
    for i in range(1, m):
        if b[i] == 0:
            b[i] = a[0]
            a.pop(0)

    print(' '.join(map(str, b)))

if __name__ == '__main__':
    main()
