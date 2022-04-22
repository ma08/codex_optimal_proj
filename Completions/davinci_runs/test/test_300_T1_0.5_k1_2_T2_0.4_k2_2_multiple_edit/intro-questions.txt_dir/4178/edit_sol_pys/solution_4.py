
def main():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] % 2 == 0:
            a[i] -= 1

    print(' '.join(map(str, a)))


if __name__ == '__main__':
    main()
