def main():
    n = int(input())
    a = list(map(int, input().split()))


    cnt = 0
    for i in range(n):
        if a[i] % 2 == 1:
            cnt += 1


    if cnt % 2 == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
