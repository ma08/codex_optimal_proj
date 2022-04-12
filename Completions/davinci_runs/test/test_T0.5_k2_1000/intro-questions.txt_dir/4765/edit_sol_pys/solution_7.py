import sys

def min_diff(s, b, n, index, curr_s, curr_b, diff, dp):
    if index == n:
        return abs(curr_s - curr_b)
    if dp[index][curr_s][curr_b] != -1:
        return dp[index][curr_s][curr_b]
    dp[index][curr_s][curr_b] = min(min_diff(s, b, n, index + 1, curr_s, curr_b, diff, dp),
                                    min_diff(s, b, n, index + 1, curr_s * s[index], curr_b + b[index], diff, dp))
    return dp[index][curr_s][curr_b]

n = int(sys.stdin.readline())
s = []
b = []
for i in range(n):
    s_i, b_i = [int(x) for x in sys.stdin.readline().split()]
    s.append(s_i)
    b.append(b_i)
dp = [[[-1 for i in range(100)] for j in range(100)] for k in range(100)]
print(min_diff(s, b, n, 0, 1, 0, 100000000, dp))
