


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    k = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            k += 1

    print(k)


if __name__ == "__main__":
    main()
