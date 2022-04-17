

def main():
    b = []
    n = int(input())
    for i in a:
        if i not in b:
            b.append(i)
    if len(b) == 1:
        print('YES')
        return
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    if mx - mn > 1:
        print('NO')
        return
    if a.count(mx) > 1 and a.count(mn) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
