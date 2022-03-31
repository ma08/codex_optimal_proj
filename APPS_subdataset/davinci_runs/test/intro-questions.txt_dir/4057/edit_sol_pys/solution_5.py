
def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    a.sort(reverse=True)

    num_bins = 0
    current_bin = 0
    for i in range(n):
        if a[i] >= current_bin:
            num_bins += 1
            current_bin = a[i] - 1

    print(num_bins)


if __name__ == "__main__":
    main()
