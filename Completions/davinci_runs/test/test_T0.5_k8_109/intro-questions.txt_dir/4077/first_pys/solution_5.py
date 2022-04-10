

from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    # counts[i] is the number of indices j such that a[j] <= i
    counts = [0] * (max(a) + 1)
    for i in range(n):
        counts[a[i]] += 1

    # partial_sums[i] is the number of indices j such that a[j] <= i
    partial_sums = [0] * (max(a) + 1)
    partial_sums[0] = counts[0]
    for i in range(1, len(partial_sums)):
        partial_sums[i] = partial_sums[i - 1] + counts[i]

    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m
    counts = [0] * (n + 1)

    for i in range(n):
        # We want to find the number of indices j such that a[j] <= m and a[j + i] >= m
        # This is equivalent to the number of indices j such that a[j] <= m and a[j + i] <= m
        # This is the number of indices j such that a[j] <= m
        # minus the number of indices j such that a[j] <= m - 1
        counts[i + 1] = partial_sums[m] - partial_sums[m - 1]

    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m
    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m + 1
    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m + 2
    # ...
    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m + i
    for i in range(1, n + 1):
        counts[i] += counts[i - 1]

    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m
    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m + 1
    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m + 2
    # ...
    # counts[i] is the number of indices j such that median(a[j], a[j + 1], ..., a[j + i]) = m + i
    print(counts[n])

main()