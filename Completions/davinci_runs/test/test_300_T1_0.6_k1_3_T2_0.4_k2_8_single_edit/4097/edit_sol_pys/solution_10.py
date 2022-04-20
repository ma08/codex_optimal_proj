

def main():
    n = int(input())
    b = [int(x) for x in input().split()]

    if n <= 2:
        print(0)
        return

    b.sort()

    min_diff = b[1] - b[0] + 1
    max_diff = b[1] - b[0] + 1
    for i in range(1, n-1):
        diff = b[i+1] - b[i] + 1
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
        diff = b[i+1] - b[i] + 1
        if diff == min_diff + 1:
            count += 1
        elif diff == min_diff - 1:
            count += 1
            b[i] -= 1
        elif diff == min_diff:
            continue
        else:
            print(-1)
            return

    for i in range(n - 1):
        if b[i+1] - b[i] + 1 != min_diff:
            print(-1)
            return

    print(count)


if __name__ == "__main__":
    main()
