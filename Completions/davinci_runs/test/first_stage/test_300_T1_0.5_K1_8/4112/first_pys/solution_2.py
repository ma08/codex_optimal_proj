

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    if x < n - k + 1:
        print(-1)
        return

    max_prefix_sum = [0] * (n + 1)
    max_suffix_sum = [0] * (n + 1)
    max_prefix_sum[0] = 0
    max_suffix_sum[n] = 0

    for i in range(1, n + 1):
        max_prefix_sum[i] = max(max_prefix_sum[i - 1] + a[i - 1], a[i - 1])

    for i in range(n - 1, -1, -1):
        max_suffix_sum[i] = max(max_suffix_sum[i + 1] + a[i], a[i])

    max_sum = 0
    for i in range(n - k + 1):
        max_sum = max(max_sum, max_prefix_sum[i] + max_suffix_sum[i + k])

    print(max_sum)

if __name__ == '__main__':
    main()