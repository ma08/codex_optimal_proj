

# SOLUTION
# This is a mathematical problem.
# We need to find the number of ways to represent n as the sum of a+b where a and b are positive integers and a>b.
# This is simply the number of pairs of integers (a,b) such that a+b=n and a>b.
# This can be found by counting the number of pairs (a,b) such that a+b=n and a>=b and subtracting the number of pairs (a,b) such that a+b=n and a<b.
# The number of pairs (a,b) such that a+b=n and a>=b is simply the number of ways to represent n as the sum of two positive integers, which is floor(n/2).
# The number of pairs (a,b) such that a+b=n and a<b is simply the number of ways to represent n as the sum of two positive integers, which is floor(n/2).
# Thus, the number of ways to represent n as the sum of a+b where a and b are positive integers and a>b is floor(n/2)-floor(n/2).
# This can be simplified to 0 for all n.

from sys import stdin, stdout

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    stdout.write(str(0)+'\n')