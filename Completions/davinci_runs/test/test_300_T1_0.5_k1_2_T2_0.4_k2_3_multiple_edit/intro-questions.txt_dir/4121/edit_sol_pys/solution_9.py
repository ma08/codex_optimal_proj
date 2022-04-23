


def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_ = max(a)
    min_ = min(a)
    if max_ == min_:
        print('YES')
        return
    if max_ - min_ > 1:
        print('NO')
        return
    if a.count(max_) > 1 and a.count(min_) > 1:
        print('NO')
        return
    print('YES')


if __name__ == "__main__":
    main()
