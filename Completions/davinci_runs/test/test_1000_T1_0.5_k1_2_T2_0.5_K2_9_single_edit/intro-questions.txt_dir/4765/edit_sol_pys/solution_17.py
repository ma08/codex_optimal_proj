
import sys

def min_diff(s, b, n, index, curr_s, curr_b, diff):
    if index == n:
        return abs(curr_s - curr_b)
    if diff < abs(curr_s - curr_b):
        return diff
    return min(min_diff(s, b, n, index + 1, curr_s, curr_b, diff),
               min_diff(s, b, n, index + 1, curr_s * s[index], curr_b + b[index], diff))

n = int(sys.stdin.readline())
s = []
b = []
for i in range(n):
    s_i, b_i = [int(x) for x in sys.stdin.readline().split()]
    s.append(s_i)
    b.append(b_i)
print(min_diff(s, b, n, 0, 1, 0, 100000000))
