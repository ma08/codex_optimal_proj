import sys

n = int(input())
prefixes = []
suffixes = []

for i in range(2*n-2):
    s = sys.stdin.readline()
    if len(s) == 1:
        prefixes.append(s)
    else:
        suffixes.append(s)

for i in range(2*n-2):
    if i < n-1:
        print("P", end="")
    else:
        print("S", end="")
