
def solve(N, d):
    d.sort()
    d_median = d[N // 2]

    l, r = 0, 0
    for i in range(N // 2):
        l += d[i]
    for i in range(N // 2, N):
        r += d[i]

    K_min = d[0]
    K_max = d[-1]

    if l == r:
        return K_max - K_min + 1

    return K_max - K_min + 1


def main():
    N = int(input())
    d = list(map(int, input().split()))

    print(solve(N, d))


if __name__ == '__main__':
    main()
