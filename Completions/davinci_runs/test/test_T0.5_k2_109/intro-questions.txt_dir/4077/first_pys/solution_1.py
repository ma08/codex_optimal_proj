


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if a[(i+j)//2] == m:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()