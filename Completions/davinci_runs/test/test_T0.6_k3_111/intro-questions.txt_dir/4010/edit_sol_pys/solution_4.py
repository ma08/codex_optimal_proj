

# SOLUTION
# Use dynamic programming
# dp[i] = [j, k, l] where j is the location of the first occurrence of i, k is the location of the last occurrence of i and l is the last occurrence of i in a palindrome
# dp = [[None]*n]*n
# dp = [[[None]*n]*n]*n
# O(n^3)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = [int(x) for x in input().strip().split()]

    dp = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = [None]*n
    # print(dp)

    for i in range(n):
        first_occurrence = None
        last_occurrence = None
        for j in range(n):
            if a[j] == a[i]:
                if first_occurrence is None:
                    first_occurrence = j
                last_occurrence = j
        dp[i][i][i] = [first_occurrence, last_occurrence, i]
        # print(dp)
    # print(dp)

    for i in range(n):
        for j in range(i+1, n):
            # print(i, j)
            if a[i] == a[j]:
                # print("a[{}] == a[{}]".format(i, j))
                dp[i][j][i] = [i, j, i]
                dp[i][j][j] = [i, j, j]
                if j-i >= 2:
                    dp[i][j][j-1] = [i, j-1, j-1]

    # print(dp)

    for k in range(2, n):
        for i in range(n-k):
            j = i+k
            # print(i, j)
            if dp[i][j-1][j-2] is not None and dp[i+1][j][j] is not None:
                if dp[i+1][j][j][0] == i:
                    dp[i][j][j-1] = [i, j-1, j-1]

            if dp[i+1][j][j-1] is not None and dp[i][j-1][j-1] is not None:
                if dp[i][j-1][j-1][1] == i:
                    dp[i][j][j] = [i, j, j]

    # print(dp)

    result = False
    for i in range(n):
        for j in range(n):
            if dp[i][j][j] is not None:
                result = True
                break
    if result:
        print("YES")
    else:
        print("NO")
