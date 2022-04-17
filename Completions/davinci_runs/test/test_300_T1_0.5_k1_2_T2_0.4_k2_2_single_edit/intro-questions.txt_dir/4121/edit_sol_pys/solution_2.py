

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        mx = max(a)
        mn = min(a)
        if mx == mn:
            print('YES')
            continue
        if mx - mn > 1:
            print('NO')
            continue
        if a.count(mx) > 1 and a.count(mn) > 1:
            print('NO')
            continue
        print('YES')


if __name__ == "__main__":
    main()
