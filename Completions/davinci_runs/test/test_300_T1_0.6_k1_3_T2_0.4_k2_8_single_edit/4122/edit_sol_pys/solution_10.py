

import math


def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    print(get_max_sum(a, k))


def get_max_sum(a, k):
    max_sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if abs(a[i] - a[j]) <= k:
                max_sum = max(max_sum, a[i] + a[j])
    return max_sum


if __name__ == "__main__":
    main()
