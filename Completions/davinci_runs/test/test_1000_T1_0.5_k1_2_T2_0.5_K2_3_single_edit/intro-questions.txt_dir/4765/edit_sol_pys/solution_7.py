import sys

def min_diff(s, b, n, index, curr_s, curr_b, diff, cache):
    if index == n:
        return abs(curr_s - curr_b), diff
    if cache[index] != -1:
        return cache[index]
    cache[index] = min(min_diff(s, b, n, index + 1, curr_s, curr_b, diff, cache)[0],
                       min_diff(s, b, n, index + 1, curr_s * s[index], curr_b + b[index], diff, cache)[0])
    return cache[index], diff

n = int(sys.stdin.readline())
s = []
b = []
for i in range(n):
    s_i, b_i = [int(x) for x in sys.stdin.readline().split()]
    s.append(s_i)
    b.append(b_i)
cache = [-1 for i in range(n)]
print(min_diff(s, b, n, 0, 1, 0, 100000000, cache)[0])
