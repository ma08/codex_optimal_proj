def main():
    n = int(input())
    x = list(map(int, input().split()))
    s = sum(x)
    if s % n:
        print(-1)
    else:
        s //= n
        if x[0] == x[-1]:
            print(0)
        else:
            c = 0
            for i in x:
                c += abs(i - s)
            print(c//2)


if __name__ == '__main__':
    main()


def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = min(x)
    x = [i - m for i in x]  # 全部減去最小值
    x.sort()  # 排序
    s = sum(x)
    if s % n:
        print(-1)
    else:
        s //= n
        if x[0] == x[-1]:
            print(0)
        else:
            c = 0
            for i in x:
                c += abs(i - s)
            print(c//2)

if __name__ == '__main__':
    main()
