

def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    mx = max(a)  # max element
    mn = min(a)  # min element
    if mx == mn:
        print('YES')
        return
    if mx - mn > 1:  # if max - min > 1 then it is not possible to have all elements equal
        print('NO')
        return
    if a.count(mx) > 1 and a.count(mn) > 1:  # if more than 1 max and min then it is not possible to have all elements equal
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
