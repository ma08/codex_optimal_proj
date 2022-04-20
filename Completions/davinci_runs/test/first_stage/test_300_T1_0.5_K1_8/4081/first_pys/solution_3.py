


def solve(n, a):
    l = [1] * n
    r = [1] * n
    for i in range(1, n):
        if a[i] > a[i - 1]:
            l[i] = l[i - 1] + 1
        else:
            l[i] = 1
    for i in reversed(range(n - 1)):
        if a[i] < a[i + 1]:
            r[i] = r[i + 1] + 1
        else:
            r[i] = 1
    r[n - 1] = 1
    ans = max(l + r)
    # print(l, r)
    return ans


def print_ans(ans):
    print(len(ans))
    print(''.join(ans))


def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = solve(n, a)
    print_ans(ans)


def test():
    assert solve(5, [2, 1, 5, 4, 3]) == 'LRRR'
    assert solve(7, [1, 3, 5, 6, 7, 4, 2]) == 'LRLRLLL'
    assert solve(3, [1, 2, 3]) == 'LLL'
    assert solve(4, [1, 2, 4, 3]) == 'LLRL'


if __name__ == "__main__":
    test()
    main()