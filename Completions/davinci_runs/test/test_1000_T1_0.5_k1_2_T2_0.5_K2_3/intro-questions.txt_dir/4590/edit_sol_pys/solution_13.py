
def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    count = 0
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < b[j]:
            k -= a[i]
            i += 1
            count += 1
        else:
            k -= b[j]
            j += 1
            count += 1
    while i < n and k >= 0:
        k -= a[i]
        i += 1
        count += 1
    while j < m and k >= 0:
        k -= b[j]
        j += 1
        count += 1
    print(count)


if __name__ == '__main__':
    main()
