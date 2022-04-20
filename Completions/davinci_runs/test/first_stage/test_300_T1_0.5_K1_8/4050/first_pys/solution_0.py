

n = int(input())
a = [int(i) for i in input().split()]

def solve():
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] + a[i-1]
    dp_dict = {}
    for i in range(1, n+1):
        if dp[i] not in dp_dict:
            dp_dict[dp[i]] = []
        dp_dict[dp[i]].append(i)
    ans = []
    for _, v in dp_dict.items():
        if len(v) > 1:
            for i in range(len(v)-1):
                ans.append((v[i], v[i+1]-1))
    ans.sort(key=lambda x: x[1]-x[0], reverse=True)
    print(len(ans))
    for i in ans:
        print(i[0], i[1])

solve()