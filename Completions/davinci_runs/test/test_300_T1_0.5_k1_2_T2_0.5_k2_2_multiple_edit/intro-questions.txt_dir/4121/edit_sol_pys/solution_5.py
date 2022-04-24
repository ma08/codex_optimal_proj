

def main():
    a = list(map(int, input().split()))
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        print('YES')
        return
    if max_a - min_a > 1:
        print('NO')
        return
    if a.count(max_a) > 1 and a.count(min_a) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
