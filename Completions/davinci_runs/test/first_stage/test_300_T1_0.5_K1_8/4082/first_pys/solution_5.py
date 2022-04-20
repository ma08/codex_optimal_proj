

def find_max_inc_subarray(a):
    n = len(a)
    dp = [1 for i in range(n)]
    for i in range(1, n):
        if a[i] > a[i-1]:
            dp[i] = dp[i-1] + 1
    return max(dp)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(find_max_inc_subarray(a))

if __name__ == '__main__':
    main()