

    # n = int(input())
    # a = list(map(int, input().split()))
    # lmin = a[0]
    # rmax = a[-1]
    # ans = 0
    # for i in range(1, n):
    #     ans = max(ans, max(a[i] - lmin, rmax - a[i]))
    #     lmin = min(lmin, a[i])
    #     rmax = max(rmax, a[i])
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += max(a[i] - a[i - 1], 0)
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += max(a[i] - a[i - 1] - 1, 0)
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += max(a[i - 1] - a[i] - 1, 0)
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += max(a[i] - a[i - 1], 0)
    # ans += max(a[0] - a[-1], 0)
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += max(a[i] - a[i - 1] - 1, 0)
    # ans += max(a[0] - a[-1] - 1, 0)
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += max(a[i - 1] - a[i] - 1, 0)
    # ans += max(a[-1] - a[0] - 1, 0)
    # print(ans)

    # n = int(input())
    # a = list(map(int, input().split()))
    # ans = 0
    # for i in range(1, n):
    #     ans += abs(a[i] - a[i - 1]) - 1
    # print(ans)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = [0] * n
    r = [0] * n
    for i in range(n):
        if i == 0:
            l[i] = a[i]
        else:
            l[i] = l[i - 1] + a[i]
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            r[i] = b[i]
        else:
            r[i] = r[i + 1] + b[i]
    print(max(l[i] + r[i] for i in range(n)))

if __name__ == '__main__':
    main()
