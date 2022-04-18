

def main():
    """
    This program is used to find the minimum number of songs to compress so that they all fit on a flash drive
    # n, m = [int(i) for i in input().split()]
    # a = []
    # b = []
    # for _ in range(n):
    #     a_i, b_i = [int(i) for i in input().split()]
    #     a.append(a_i)
    #     b.append(b_i)
    # # a.sort()
    # # b.sort()
    # a_sum = sum(a)
    # b_sum = sum(b)
    # if a_sum <= m:
    #     print(0)
    # elif b_sum > m:
    #     print(-1)
    # else:
    #     i = 0
    #     while a_sum > m:
    #         a_sum -= a[i]-b[i]
    #         i += 1
    #     print(i)
    """
    n, m = [int(i) for i in input().split()]
    a = [0]*(n+1)
    b = [0]*(n+1)
    for _ in range(n):
        a[i+1], b[i+1] = [int(i) for i in input().split()]

    a_sum = [0]*(n+1)
    b_sum = [0]*(n+1)
    for i in range(1, n+1):
        a_sum[i] = a_sum[i-1]+a[i]
        b_sum[i] = b_sum[i-1]+b[i]

    ans = 0
    for i in range(1, n+1):
        if a_sum[i] <= m:
            ans = i
        if a_sum[i] > m:
            break
    print(ans)


if __name__ == "__main__":
    main()
