


def main():
    n = int(input())
    a = input()
    f = [int(x) for x in input().split()]

    max_num = 0
    max_idx = 0
    for i in range(n):
        if int(a[i]) == max(f):
            max_num = max(max_num, int(a[i:]))
            max_idx = i
            break

    for i in range(n - 1, -1, -1):
        if int(a[i]) == max(f):
            max_num = max(max_num, int(a[:i + 1]))

    print(max_num)


if __name__ == "__main__":
    main()