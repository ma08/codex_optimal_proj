

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        print('NO')
    else:
        if a[0] % 2 == 0 or a[-1] % 2 == 0:
            print('NO')
        else:
            print('YES')


if __name__ == "__main__":
    main()
