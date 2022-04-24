def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 == 1:
        print('NO')
        exit()


    for i in range(n // 2):
        if a[2 * i] != a[2 * i + 1]:
            print('NO')
            exit()

    print('YES')

if __name__ == '__main__':
    main()
