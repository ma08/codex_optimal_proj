# Problem
# You are given an array of N positive integers, A1, A2 ,…, AN.
# Find the sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
# f(x, y) is defined as
# f(x, y) = (x & y) + (x | y) + (x ^ y), where &, | and ^ are the bitwise AND, OR and XOR operators respectively.

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
