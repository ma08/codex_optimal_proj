
import sys

def min_diff(s, b, n, index, curr_s, curr_b, min_diff_so_far): # s = s_i, b = b_i, n = n, index = i, curr_s = s, curr_b = b, min_diff_so_far = best
    if index == n: # if i == n
        return abs(curr_s - curr_b) # return |s - b|
    if min_diff_so_far < abs(curr_s - curr_b): # if best < |s - b|
        return min_diff_so_far # return best
    return min(min_diff(s, b, n, index + 1, curr_s, curr_b, min_diff_so_far), # return min(min_diff(s_i, b_i, n, i+1, s, b, best),
               min_diff(s, b, n, index + 1, curr_s * s[index], curr_b + b[index], min_diff_so_far)) # min_diff(s_i, b_i, n, i+1, s * s_i, b + b_i, best))

n = int(sys.stdin.readline()) # n = int(input())
s = [] # s = []
b = [] # b = []
for i in range(n): # for i in range(n):
    s_i, b_i = [int(x) for x in sys.stdin.readline().split()] # s_i, b_i = [int(x) for x in input().split()]
    s.append(s_i) # s.append(s_i)
    b.append(b_i) # b.append(b_i)
print(min_diff(s, b, n, 0, 1, 0, 100000000)) # print(min_diff(s, b, n, 0, 1, 0, 100000000))
