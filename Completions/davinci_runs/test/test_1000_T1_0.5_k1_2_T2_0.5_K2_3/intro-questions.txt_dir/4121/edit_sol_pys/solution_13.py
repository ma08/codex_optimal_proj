

def main():
    _ = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if (a[-1] - a[0]) <= 1:
        print('YES' if a.count(a[-1]) == 1 or a.count(a[0]) == 1 else 'NO')
    else:
        print('NO')


if __name__ == "__main__":
    main()
