def get_input():
    n = [int(x) for x in input().split()]
    k = int(input())
    return n, k

def get_value(n, k, dp):
    if n[0] == 0:
        return 0
    if dp[n[0]][k] == -1:
        if k == 1:
            dp[n[0]][k] = n[0]
        elif k == 2:
            dp[n[0]][k] = n[0] * (n[0] - 1) / 2
        else:
            dp[n[0]][k] = sum([get_value(n[1:], k-1, dp) * n[0] for i in range(k)])
    return dp[n[0]][k]

def get_answer(n, k):
    dp = [[-1 for i in range(k + 1)] for j in range(len(n) + 1)]
    return int(get_value(n, k, dp))

def main():
    n, k = get_input()
    print(get_answer(n, k))

if __name__ == "__main__":
    main()
