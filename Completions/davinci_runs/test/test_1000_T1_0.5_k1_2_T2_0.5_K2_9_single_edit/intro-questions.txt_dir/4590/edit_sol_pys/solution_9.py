


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    count = 0
    i = 0
    j = 0
        if a[i] >= b[j]:
            k -= a[i]
            i += 1
            count += 1
        else:
            k -= b[j]
            j += 1
            count += 1
    if i < n:
        count += n-i
    if j < m:
        count += m-j
    print(count)


if __name__ == '__main__':
    main()
