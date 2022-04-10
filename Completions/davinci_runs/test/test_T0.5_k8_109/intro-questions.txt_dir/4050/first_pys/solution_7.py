

def solve(arr):
    n = len(arr)
    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1] + arr[i-1]
    dp = set(dp)
    # print(dp)
    dp = list(dp)
    dp.sort()
    # print(dp)
    dp2 = {}
    for i in range(len(dp)):
        dp2[dp[i]] = i
    # print(dp2)
    dp3 = [0]*(n+1)
    for i in range(1,n+1):
        dp3[i] = dp2[dp3[i-1] + arr[i-1]]
    # print(dp3)
    dp4 = [0]*(n+1)
    ans = []
    for i in range(1,n+1):
        dp4[i] = dp4[i-1]
        if dp3[i] != dp3[i-1]:
            dp4[i] += 1
            ans.append([i,i])
    # print(dp4)
    # print(dp4[-1])
    # print(ans)
    dp5 = [0]*(n+1)
    for i in range(1,n+1):
        dp5[i] = dp5[i-1]
        if dp3[i] != dp3[i-1]:
            dp5[i] += 1
    # print(dp5)

    dp6 = [0]*(n+1)
    for i in range(1,n+1):
        dp6[i] = dp6[i-1]
        if dp5[i] == dp4[i]:
            dp6[i] += 1
    # print(dp6)
    # print(dp6[-1])
    # print(ans)

    dp7 = [0]*(n+1)
    for i in range(1,n+1):
        dp7[i] = dp7[i-1]
        if dp6[i] == dp6[i-1]:
            dp7[i] += 1
    # print(dp7)
    # print(dp7[-1])
    # print(ans)

    print(dp7[-1])
    for i in range(dp7[-1]):
        print(ans[i][0],ans[i][1])


n = int(input())
arr = list(map(int,input().split()))
solve(arr)