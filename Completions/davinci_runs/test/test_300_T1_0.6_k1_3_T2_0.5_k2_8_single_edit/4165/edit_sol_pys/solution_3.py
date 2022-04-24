
import sys

n = int(input())
line = input().split()
line = [int(i) for i in line]  # list comprehension

# print(n, line)

if max(line) < sum(line) - max(line):
    print("Yes")
else:
    print("No")
