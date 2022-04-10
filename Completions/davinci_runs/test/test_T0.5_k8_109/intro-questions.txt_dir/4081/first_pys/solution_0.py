

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # find the longest increasing subsequence
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lis[i] <= lis[j]:
                lis[i] = lis[j] + 1

    # find the longest decreasing subsequence
    lds = [1] * n
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if a[i] > a[j] and lds[i] <= lds[j]:
                lds[i] = lds[j] + 1

    # find the longest common subsequence
    lcs = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and lcs[i] <= lcs[j]:
                lcs[i] = lcs[j] + 1

    # find the longest alternating subsequence
    la = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and la[i] <= la[j]:
                la[i] = la[j] + 1
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if a[i] > a[j] and la[i] <= la[j]:
                la[i] = la[j] + 1

    # find the maximum length of any subsequence
    print(max(lis + lds + lcs + la))


if __name__ == '__main__':
    main()