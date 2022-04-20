


def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    a.sort()
    max_count = 0
    i = 0
    while i < n:
        count = 1
        j = i + 1
        while j < n and a[j] <= a[i] + 5:
            count += 1
            j += 1
        if count > max_count:
            max_count = count
        i += 1
    print(max_count)


if __name__ == '__main__':
    main()