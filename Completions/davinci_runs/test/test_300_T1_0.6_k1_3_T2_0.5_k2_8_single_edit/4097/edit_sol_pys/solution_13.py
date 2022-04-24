

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    if n <= 2:
        print(0)
        return

    a.sort()

    min_diff = a[1] - a[0]
    max_diff = a[1] - a[0]
    for i in range(1, n-1):
        diff = a[i+1] - a[i]
        if diff < min_diff:
            min_diff = diff
        if diff > max_diff:
            max_diff = diff

    if min_diff == max_diff:
        print(0)
        return

    if max_diff - min_diff > 1:
        print(-1)
        return

    if min_diff == 0:
        print(1)
        return

    count = 0
    for i in range(n - 1):
        diff = a[i+1] - a[i]
        if diff == min_diff + 1:
            count += 1
        elif diff == min_diff - 1:
            count += 1
            a[i] -= 1
        elif diff == min_diff:
            continue
        else:
            print(-1)
            return

    for i in range(n - 1):
        if a[i+1] - a[i] != min_diff:
            print(-1)
            return

    print(count)


if __name__ == "__main__":
    main()
