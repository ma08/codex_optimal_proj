

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] == a[0]:
        print('YES')
        return
    if a[-1] - a[0] > 1:
        print('NO')
        return
    if a.count(a[-1]) > 1 and a.count(a[0]) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
