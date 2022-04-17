# Problem
# Given an array of integers, find and print its number of unique elements.
#
# For example, the array arr = [1, 2, 1, 3, 2, 3] has elements 1, 2, 3 appearing twice each, while the unique elements are 1, 2, and 3.
#
# Function Description
#
# Complete the lonelyinteger function in the editor below. It should return the integer which appears only once in the input array.
#
# lonelyinteger has the following parameter(s):
#
# a: an array of integers
# Input Format
#
# The first line contains a single integer, n, denoting the number of integers in the array.
# The second line contains n space-separated integers describing the respective values in arr.
#
# Constraints
#
# 1 <= n <= 100
#
# 1 <= a[i] <= 100
#
# Output Format
#
# Print the unique number that occurs only once in  on a new line.
#
# Sample Input 0
#
# 1
# 1
# Sample Output 0
#
# 1
# Explanation 0
#
# The array only contains a single 1, so we print 1 as our answer.
#
# Sample Input 1
#
# 3
# 1 1 2
# Sample Output 1
#
# 2
# Explanation 1
#
# We have two 1's and one 2. We print 2, because that's the only unique element in the array.
#
# Sample Input 2
#
# 5
# 0 0 1 2 1
# Sample Output 2
#
# 2
# Explanation 2
#
# We have two 0's, two 1's, and one 2. We print 2, because that's the only unique element in the array.

# Solution

n = int(input())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])

print(n-len(s))
