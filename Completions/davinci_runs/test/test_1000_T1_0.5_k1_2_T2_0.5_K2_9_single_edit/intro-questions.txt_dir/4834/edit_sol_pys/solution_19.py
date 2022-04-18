


def get_min_time(n, times):
    times.sort()

    total = 0
    for i in range(n):
        total += (n - i) * times[i]

    return total


def main():
    n = int(input())
    times = [int(x) for x in input().split()]

    print(get_min_time(n, times))


if __name__ == '__main__':
    main()
