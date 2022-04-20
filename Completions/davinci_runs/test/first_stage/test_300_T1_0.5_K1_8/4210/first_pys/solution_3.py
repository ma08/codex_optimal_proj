


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    res = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if int(str(a[i]) + str(a[j])) % k == 0:
                res += 1

    print(res)


if __name__ == '__main__':
    main()