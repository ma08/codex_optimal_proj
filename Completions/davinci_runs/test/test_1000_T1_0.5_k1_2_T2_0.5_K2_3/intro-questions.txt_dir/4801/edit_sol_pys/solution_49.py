

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [a[0]]  # list of the last element of the increasing subsequences
    for i in range(1, n):
        if a[i] > dp[-1]:  # if a[i] is greater than the last element of the increasing subsequences, then it is the last element of a new increasing subsequence
            dp.append(a[i])
        else:  # otherwise, find the first element that is greater than or equal to a[i] in the increasing subsequences, and replace it with a[i]
            for j in range(len(dp)):
                if dp[j] >= a[i]:
                    dp[j] = a[i]
                    break
    print(len(dp))
    print(*dp)


solve()
