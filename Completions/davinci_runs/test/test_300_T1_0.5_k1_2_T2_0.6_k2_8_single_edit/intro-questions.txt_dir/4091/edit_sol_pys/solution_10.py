


class Solution:
    def __init__(self):
        self.dp = {}

    def fib(self, n):
        if n == 0 or n == 1:
            return n
        if n in self.dp:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]

print(Solution().fib(5))
