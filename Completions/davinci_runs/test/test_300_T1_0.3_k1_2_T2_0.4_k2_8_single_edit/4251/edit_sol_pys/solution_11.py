

# Problem

# You are given a sequence of N (1≤N≤100) integers A1,A2,…,AN.
# You want to partition the sequence into some number of (not necessarily contiguous) subsequences,
# such that each element appears in exactly one of the subsequences.
#
# The sum of the elements in a subsequence must be greater than or equal to M (1≤M≤10^9).
#
# Find the maximum number of subsequences that you can obtain.

# Input
# The first line of the input contains two space-separated integers N and M.
#
# The second line contains N space-separated integers A1,A2,…,AN.
#
# Output
# Print a single line containing one integer ― the maximum number of subsequences that you can obtain.
#
# Examples
# Input
# 5 2
# 2 1 4 5 3
# Output
# 3
#
# Input
# 8 3
# 1 1 1 1 1 1 1 1
# Output
# 5
#
# Note
# In the first sample, one optimal solution is to partition the sequence into the subsequences {2}, {1,4}, and {5,3}.
#
# In the second sample, one optimal solution is to partition the sequence into the subsequences {1,1,1}, {1,1,1}, {1,1}, {1}, and {1}.

# Solution

def solve(n, m, a):
    a.sort(key=lambda x: x[0])
    ans = 0
    for i in range(1, n):
        ans = max(ans, a[i][0] - a[i-1][0])
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(solve(n, m, a))
