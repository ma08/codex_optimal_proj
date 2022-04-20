
def main():
    n, m = map(int, input().split())
    if n == 1:
        print(1)
        return
    if mx - mn > 1:
        print('NO')
        return
    if a.count(mx) > 1 and a.count(mn) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
