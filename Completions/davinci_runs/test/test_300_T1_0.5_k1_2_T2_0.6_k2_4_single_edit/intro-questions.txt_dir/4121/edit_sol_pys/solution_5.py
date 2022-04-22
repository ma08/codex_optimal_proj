

def main():
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    if mx == mn: return print('YES')
    if mx - mn > 1: return print('NO')
    if a.count(mx) > 1 and a.count(mn) > 1: return print('NO')
    return print('YES')


if __name__ == "__main__":
    main()
