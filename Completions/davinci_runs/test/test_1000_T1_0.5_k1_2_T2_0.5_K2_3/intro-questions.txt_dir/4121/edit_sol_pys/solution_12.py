

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    if mx == mn:
        print('YES')
        return
    if mx - mn > 1:  # if max - min > 1 then it is not possible to have all elements equal
        print('NO')
        return
    if a.count(mx) > 1 or a.count(mn) > 1:  # if more than 1 max and min then it is not possible to have all elements equal
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
