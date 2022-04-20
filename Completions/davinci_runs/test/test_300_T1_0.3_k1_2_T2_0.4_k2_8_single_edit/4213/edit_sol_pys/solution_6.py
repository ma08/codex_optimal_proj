


def main():
    n = int(input())
    array = list(map(int, input().split()))
    max_diff = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(array[i] - array[j])
            if diff > max_diff:
                max_diff = diff
    print(max_diff)


if __name__ == '__main__':
    main()
