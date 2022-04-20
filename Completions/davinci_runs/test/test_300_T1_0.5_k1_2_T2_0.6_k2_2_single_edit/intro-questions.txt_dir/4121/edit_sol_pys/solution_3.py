

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0
    mn = 0
    if len(set(a)) == 1:
        print('YES')
        return
    if abs(max(a) - min(a)) > 1:
        print('NO')
        return
    if a.count(mx) > 1 and a.count(mn) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
