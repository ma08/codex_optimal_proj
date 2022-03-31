


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    num_bins = 1
    current_bin = a[0]
    for i in range(1, n):
        if a[i] >= current_bin:
            num_bins += 1
            current_bin = a[i]

    print(num_bins)


if __name__ == "__main__":
    main()
