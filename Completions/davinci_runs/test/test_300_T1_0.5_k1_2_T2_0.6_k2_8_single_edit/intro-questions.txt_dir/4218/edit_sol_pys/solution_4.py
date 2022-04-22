def main():
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]


    f, s = 0, 0
    for i in range(n):
        if i % 2 == 0:
            f += a[i]
        else:
            s += a[i]
    print(f - s)


if __name__ == '__main__':
    main()
