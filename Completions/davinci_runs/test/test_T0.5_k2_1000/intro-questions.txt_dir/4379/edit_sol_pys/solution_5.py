
import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def main():
    n = read_int()
    a = read_ints()
    a.insert(0, -1)  # a[0] = -1, so that we can start from 1

    dp = [1] * (n + 1)  # dp[i] = length of longest increasing subsequence ending at a[i]
    prev = [0] * (n + 1)  # prev[i] = previous index of longest increasing subsequence ending at a[i]

    for i in range(1, n + 1):  # iterate over all indices
        for j in range(i - 1, 0, -1):  # iterate over all previous indices
            if a[j] < a[i]:  # if previous index is smaller than current index
                if dp[j] + 1 > dp[i]:  # if longest increasing subsequence ending at a[j] is longer than longest increasing subsequence ending at a[i]
                    dp[i] = dp[j] + 1  # update longest increasing subsequence ending at a[i]
                    prev[i] = j  # update previous index of longest increasing subsequence ending at a[i]

    max_len = max(dp)
    max_index = dp.index(max_len)

    ans = [max_index]
    while prev[max_index] != 0:
        max_index = prev[max_index]
        ans.append(max_index)

    print(max_len)
    print(' '.join(map(str, reversed(ans))))

if __name__ == '__main__':
    main()
