
import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def main():
    n = read_int()
    a = [-1] + read_ints()

    dp = [1] * (n + 1)
    prev = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            if a[j] < a[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

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
