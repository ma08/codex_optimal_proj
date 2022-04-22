def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n):
        if a[i - 1] > a[i]:
            a[i] += 1

    for i in range(1, n):
        if a[i - 1] > a[i]:
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    main()
