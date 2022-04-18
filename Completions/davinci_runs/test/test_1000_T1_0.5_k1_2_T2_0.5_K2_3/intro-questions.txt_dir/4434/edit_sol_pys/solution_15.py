

# SOLUTION
# The problem can be solved with dynamic programming.
# Let f(n) be the number of moves to solve the problem for a board of size n x n.
# f(n) = f(n - 2) + 4, for n > 2, because the last two rows and the last two columns
# can be solved in four moves.
# f(n) = 0, for n = 0 or n = 2, because the board is already solved.
# The time complexity is O(n), which is the number of moves.

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0, 0, 0]
    for i in range(3, n + 1):
        dp.append(dp[i - 2] + 4)
    print(dp[n])
