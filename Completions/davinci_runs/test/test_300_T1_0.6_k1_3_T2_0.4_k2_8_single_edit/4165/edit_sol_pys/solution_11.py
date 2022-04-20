
import sys

n = int(input())
line = list(map(int, input().split()))

print(n, line)

if max(line) < sum(line) - max(line):
    print("Yes")
else:
    print("No")
