

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)  # mx = 4
    mn = min(a)  # mn = 1
    if mx == mn:  # 4 == 1
        print('YES')
        return
    if mx - mn > 1:  # 4 - 1 > 1
        print('NO')
        return
    if a.count(mx) > 1 or a.count(mn) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
