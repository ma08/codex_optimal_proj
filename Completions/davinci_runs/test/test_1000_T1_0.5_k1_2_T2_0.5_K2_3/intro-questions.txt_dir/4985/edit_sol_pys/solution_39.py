

import sys
sys.stdin = open('input.txt')

# read input
n, m = map(int, sys.stdin.readline().split())

# initialize variables
c = []
for i in range(n):
    c.append(sys.stdin.readline().rstrip())

# loop to find the shortest string
s = c[0]
for i in range(1, n):
    if len(c[i]) < len(s):
        s = c[i]

# print
print(s)









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# initialize variables
c = []
for i in range(n):
    c.append(input())

# loop to find the shortest string
s = c[0]
for i in range(1, n):
    if len(c[i]) < len(s):
        s = c[i]

# print
print(s)
