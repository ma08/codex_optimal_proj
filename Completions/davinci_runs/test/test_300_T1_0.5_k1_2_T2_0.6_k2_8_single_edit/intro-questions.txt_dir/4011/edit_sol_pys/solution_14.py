


def main(n, num, f):
    for i in range(n):
        num[i] = f[num[i]-1]
    return ''.join(map(str, num))


if __name__ == '__main__':
    main()
