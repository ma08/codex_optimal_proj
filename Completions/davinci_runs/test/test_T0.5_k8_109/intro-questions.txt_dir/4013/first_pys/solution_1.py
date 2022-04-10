


def main():
    n = int(input())
    a = list(map(int, input().split()))

    min_value = min(a)
    max_value = max(a)
    min_index = a.index(min_value)
    max_index = a.index(max_value)

    if min_index < max_index:
        print(max_value - min(a[:min_index] + a[min_index + 1:]))
    else:
        print(max(a[:max_index] + a[max_index + 1:]) - min_value)


if __name__ == '__main__':
    main()