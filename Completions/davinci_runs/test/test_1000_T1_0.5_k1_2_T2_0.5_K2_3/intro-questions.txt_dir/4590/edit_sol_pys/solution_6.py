def solve(n, a):
    ans = 0
    for i in range(1, n):
        if a[i] < a[i - 1]:
            ans += a[i - 1] - a[i]
            a[i] = a[i - 1]
    return ans



def solve2(n, a):
    ans = 0
    max_a = 0
    for i in range(1, n):
        if a[i - 1] > max_a:
            max_a = a[i - 1]
        if max_a > a[i]:
            ans += max_a - a[i]
    return ans


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
    print(solve2(n, a))


if __name__ == '__main__':
    main()
