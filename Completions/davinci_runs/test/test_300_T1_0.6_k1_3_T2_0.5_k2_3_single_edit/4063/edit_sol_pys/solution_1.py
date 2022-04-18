


def solve(N, d):
    d.sort()  # O(NlogN)
    d_median = d[N // 2]  # O(1)

    l, r = 0, 0  # O(1)
    for i in range(N // 2):
        l += d[i]  # O(N)
    for i in range(N // 2, N):
        r += d[i]  # O(N)

    K_min = d[0]  # O(1)
    K_max = d[-1]  # O(1)

    if l == r:
        return K_max - K_min + 1

    return 0


def main():
    N = int(input())
    d = list(map(int, input().split()))

    print(solve(N, d))


if __name__ == '__main__':
    main()
