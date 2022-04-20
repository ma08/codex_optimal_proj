

"""
-----TODO-----
-
"""

"""
-----Solution-----
"""

# This code is for the purpose of importing faster input/output methods.
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

# Your code goes here.

N, K = map(int, input().split())

if N % K == 0:
    print(0)
else:
    print(min(N % K, K - N % K))
