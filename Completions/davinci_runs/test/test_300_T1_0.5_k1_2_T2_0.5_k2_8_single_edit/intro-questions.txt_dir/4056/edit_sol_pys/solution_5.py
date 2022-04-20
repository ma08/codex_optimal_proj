

# Problem

# Given an array A of N integers, find the GCD of all the elements of the array.
#
# Input:
# First line of input contains number of testcases T. For each testcase, there will be two lines, first of which contains N, size of array. The second line contains the elements of the array.
#
# Output:
# For each testcase, print the GCD of array elements.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 106
# 1 <= Ai <= 106
#
# Example:
# Input:
# 1
# 2
# 5 10
#
# Output:
# 5
#
# Explanation:
# Testcase 1: GCD of elements in the array is 5.


# Solution

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))

g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])

print(g)
