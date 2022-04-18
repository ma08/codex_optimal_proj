

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]]
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            for j in range(len(dp)):
                if dp[j] >= arr[i]:
                    dp[j] = arr[i]
                    break
    print(len(dp))
    print(*dp)

solve()
