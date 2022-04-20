


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    i = 0
    j = 0
    ans = 0
    while i < n:
        while j < n and a[j] <= a[i] * 2:
            j += 1
        ans = max(ans, j - i)
        i += 1
    print(ans)


if __name__ == '__main__':
    main()