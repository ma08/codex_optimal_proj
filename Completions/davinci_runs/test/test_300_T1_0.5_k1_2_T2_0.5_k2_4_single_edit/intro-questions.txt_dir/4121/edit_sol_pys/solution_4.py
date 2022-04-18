

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    if mx == 1:
        print('YES')
        return
    if mx > 1:
        print('NO')
        return
    if a.count(mx) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
