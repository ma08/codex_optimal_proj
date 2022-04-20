

# Problem

# You are given a sequence a1, a2, ..., aN. Find the maximum possible value of ai XOR aj, where 1 ≤ i, j ≤ N.

# Input

# The first line of the input contains two integers, N and K, separated by a single space.

# The second line contains N integers, a1, a2, ..., aN, separated by spaces.

# Output

# Output a single line containing the maximum possible XOR value.

# Constraints

# 2 ≤ N ≤ 10^5

# 1 ≤ K ≤ 10^9

# 0 ≤ ai ≤ K

# Example

# Input:
# 4 2
# 1 2 3 4

# Output:
# 7

# Input:
# 5 4
# 2 2 2 2 2

# Output:
# 3

# Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 0:
    print(0)
else:
    if k == 1:
        print(max(a))
    else:
        print(max(a) - min(a) + 1)
