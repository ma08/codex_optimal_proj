


def main():
    n = int(input())
    if n <= 2:
        print(0)
        return
    b = list(map(int, input().split()))
    diff = b[1] - b[0]
    for i in range(2, n):
        if b[i] - b[i-1] != diff:
            if b[i-1] - b[i-2] == diff:
                b[i] = b[i-1] + diff
            elif b[i-2] - b[i-1] == diff:
                b[i-1] = b[i-2] + diff
            else:
                print(-1)
                return
    print(b.count(b[0]) + b.count(b[-1]))


if __name__ == '__main__':
    main()