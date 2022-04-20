


def main():
    N = int(input())
    a = list(map(int, input().split()))
    max_f = 0
    for i in range(1, N+1):
        f = 0
        for j in a:
            f += i % j
        max_f = max(max_f, f)
    print(max_f)


if __name__ == '__main__':
    main()