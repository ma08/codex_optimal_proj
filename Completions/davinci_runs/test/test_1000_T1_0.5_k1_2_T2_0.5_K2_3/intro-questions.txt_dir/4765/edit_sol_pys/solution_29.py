import sys

def min_diff(s, b, n, index, curr_s, curr_b, min_diff_so_far, memo):
    if index == n:
        return abs(curr_s - curr_b)
    if min_diff_so_far < abs(curr_s - curr_b):
        return min_diff_so_far
    if memo[index][curr_s][curr_b] != -1:
        return memo[index][curr_s][curr_b]
    memo[index][curr_s][curr_b] = min(min_diff(s, b, n, index + 1, curr_s, curr_b, min_diff_so_far, memo),
                                      min_diff(s, b, n, index + 1, curr_s * s[index], curr_b + b[index], min_diff_so_far, memo))
    return memo[index][curr_s][curr_b]

n = int(sys.stdin.readline())
s = []
b = []
for i in range(n):
    s_i, b_i = [int(x) for x in sys.stdin.readline().split()]
    s.append(s_i)
    b.append(b_i)
memo = [[[-1 for _ in range(10000)] for _ in range(10000)] for _ in range(n + 1)]
print(min_diff(s, b, n, 0, 1, 0, 100000000, memo))
