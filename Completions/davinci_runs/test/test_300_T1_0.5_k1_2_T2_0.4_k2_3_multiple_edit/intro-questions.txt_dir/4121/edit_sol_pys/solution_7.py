

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    if mx == mn or mx - mn > 1 or a.count(mx) > 1 or a.count(mn) > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    main()
